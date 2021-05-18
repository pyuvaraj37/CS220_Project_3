from sklearn.ensemble import RandomForestClassifier
from DataLoad import Data
import numpy as np
import os
import time

from torchvision import models
from torchsummary import summary
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

def quantization(x, m, i):
    x = int(1 << i) * x;
    largest_signed_int = (1 << (m - 1)) - 1;
    x = min(largest_signed_int, x);
    smallest_signed_int = -(1 << (m - 1));
    x = max(smallest_signed_int, x);
    largest_unsigned_int = (1 << m) - 1;
    x = x & largest_unsigned_int;
    return format(x, 'b').zfill(m);

def retrieveData(directory):
    data = [];
    return data

def generateRandomForrest(directory):
    
    #Retrieve activations from directory:
    #May need to quantize activations, but since its a BNN possibly not.
    #From Layer 1 to Layer N-1, within every node, 
    #using the activations of the previous layer as features X_train, 
    #and the nodes activation as Y_train
    #create a random forest
    x_train, y_train = retrieveData(directory);
    randomForests = []
    
    for layer in layers:
        for node in layer:
            clf = RandomForestClassifier(n_estimators = 100)
            clf.fit(x_train[layer - 1], y_train[node])
            randomForests[layer].append(clf)

    return randomForests; 

assert os.path.exists(MODEL_PATH), "Train a model first"
lbcnn_depth, state_dict = torch.load(MODEL_PATH)
model = Lbcnn(depth=lbcnn_depth)
model.load_state_dict(state_dict) 
vgg = models.vgg16()
summary(vgg, (3, 224, 224))
        
