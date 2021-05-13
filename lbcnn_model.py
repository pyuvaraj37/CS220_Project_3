import torch
import torch.nn as nn
import torch.nn.functional as F
import numpy as np

#Credit for BNN Model https://github.com/dizcza/lbcnn.pytorch/blob/master/lbcnn_model.py
class ConvLBP(nn.Conv2d):
    def __init__(self, in_channels, out_channels, kernel_size=3, sparsity=0.5):
        super().__init__(in_channels, out_channels, kernel_size, padding=1, bias=False)
        weights = next(self.parameters())
        matrix_proba = torch.FloatTensor(weights.data.shape).fill_(0.5)
        binary_weights = torch.bernoulli(matrix_proba) * 2 - 1
        mask_inactive = torch.rand(matrix_proba.shape) > sparsity
        binary_weights.masked_fill_(mask_inactive, 0)
        weights.data = binary_weights
        weights.requires_grad_(False)


class BlockLBP(nn.Module):

    def __init__(self, numChannels, numWeights, sparsity=0.5):
        super().__init__()
        self.batch_norm = nn.BatchNorm2d(numChannels)
        self.conv_lbp = ConvLBP(numChannels, numWeights, kernel_size=3, sparsity=sparsity)
        self.conv_1x1 = nn.Conv2d(numWeights, numChannels, kernel_size=1)

    def forward(self, x):
        residual = x
        x = self.batch_norm(x)
        x = F.relu(self.conv_lbp(x))
        x = self.conv_1x1(x)
        x.add_(residual)
        return x


class Lbcnn(nn.Module):
    def __init__(self, nInputPlane=3, numChannels=16, numWeights=16, full=50, depth=2, sparsity=0.5):
        super().__init__()

        self.preprocess_block = nn.Sequential(
            nn.Conv2d(nInputPlane, numChannels, kernel_size=3, padding=1),
            nn.BatchNorm2d(numChannels),
            nn.ReLU(inplace=True)
        )
        
        chain = [BlockLBP(numChannels, numWeights, sparsity) for i in range(depth)]
        self.chained_blocks = nn.Sequential(*chain)
        self.pool = nn.AvgPool2d(kernel_size=8, stride=8)

        self.dropout = nn.Dropout(0.5)
		
        self.fc1 = nn.Linear(16*4*4, full)
        self.fc2 = nn.Linear(full, 1)

    def forward(self, x):
        x = self.preprocess_block(x)
        x = self.chained_blocks(x)
        x = self.pool(x)
        x = x.view(x.shape[0], 16*4*4)
        x = self.dropout(x)
        x = self.fc1(x)
        x = F.relu(x)
        x = self.fc2(self.dropout(x))
        return x
