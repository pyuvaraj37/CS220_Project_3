from DataLoad import Data
import numpy as np
import os
import time

import torch
import torch.nn as nn
import torch.optim as optim
import torch.optim.lr_scheduler
import torch.utils.data
from tqdm import tqdm
from DataLoad import Data

from lbcnn_model import Lbcnn
from utils import calc_accuracy, get_CIFAR_Data

MODEL_PATH = os.path.join(os.path.dirname(__file__), 'BNN Model', 'lbcnn_best.pt')

#Batches, Labels, LabelNames = Data()

def test( trainX, trainY, testX, testY, model=None):
    if model is None:
        assert os.path.exists(MODEL_PATH), "Train a model first"
        lbcnn_depth, state_dict = torch.load(MODEL_PATH)
        model = Lbcnn(depth=lbcnn_depth)
        model.load_state_dict(state_dict)
    loader = get_CIFAR_Data(trainX = trainX, trainY = trainY, testX = testX, testY = testY, train=False)
    accuracy = calc_accuracy(model, loader=loader, verbose=True) # Need to change
    print("CIFAR test accuracy: {:.3f}".format(accuracy))

def train(trainX, trainY, testX, testY, n_epochs=50, lbcnn_depth=2, learning_rate=1e-2, momentum=0.9, weight_decay=1e-4, lr_scheduler_step=5):
    start = time.time()
    models_dir = os.path.dirname(MODEL_PATH)
    if not os.path.exists(models_dir):
        os.makedirs(models_dir)

    train_loader = get_CIFAR_Data(trainX = trainX, trainY = trainY, testX = testX, testY = testY, train=True)
    test_loader = get_CIFAR_Data(trainX = trainX, trainY = trainY, testX = testX, testY = testY, train=False)
    model = Lbcnn(depth=lbcnn_depth)
    use_cuda = torch.cuda.is_available()
    if use_cuda:
        model = model.cuda()
    best_accuracy = 0.
    criterion = nn.CrossEntropyLoss()
    optimizer = optim.SGD(filter(lambda param: param.requires_grad, model.parameters()), lr=learning_rate,
                          momentum=momentum, weight_decay=weight_decay, nesterov=True)

    scheduler = optim.lr_scheduler.StepLR(optimizer, step_size=lr_scheduler_step)
    for epoch in range(n_epochs):
        for batch_id, batch in enumerate(tqdm(train_loader, desc="Epoch {}/{}".format(epoch, n_epochs))):
            inputs, labels = batch["image"], batch["label"]
            if use_cuda:
                inputs = inputs.cuda()
                labels = labels.cuda()
            optimizer.zero_grad()
            outputs = model(inputs)
            loss = criterion(outputs, labels)
            loss.backward()
            optimizer.step()
        accuracy_train = calc_accuracy(model, loader=train_loader)
        accuracy_test = calc_accuracy(model, loader=test_loader)
        print("Epoch {} accuracy: train={:.3f}, test={:.3f}".format(epoch, accuracy_train, accuracy_test))
        if accuracy_train > best_accuracy:
            best_accuracy = accuracy_train
            torch.save((lbcnn_depth, model.state_dict()), MODEL_PATH)
        scheduler.step(epoch=epoch)
    train_duration_sec = int(time.time() - start)
    print('Finished Training. Total training time: {} sec'.format(train_duration_sec))


if __name__ == '__main__':
    # train includes test phase at each epoch
    Batches, Label, LabelNames = Data()
    train(n_epochs=20, trainX = Batches[0], trainY = Label[0], testX = Batches[1], testY = Label[1])
