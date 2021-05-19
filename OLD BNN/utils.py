import torch
import torch.utils.data
import torchvision
import torchvision.transforms as transforms
from tqdm import tqdm
import numpy as np
from DataLoad import Data

class CIFARIMAGEDATASET():
	def __init__(self, X, Y, transform = None):
		self.Batches, self.Labels = X, Y
		self.transform = transform
		
	def __len__(self):
		return len(self.Labels)
		
	def __getitem__(self, idx):
		image = np.array(self.Batches[idx])
		image = image.reshape(32,32, 3)
		label = torch.tensor(self.Labels[idx],dtype=torch.long)
		if self.transform:
			image = self.transform(image)
		sample = {'image': image, 'label': label}
		return sample



def get_CIFAR_Data(trainX, trainY, testX, testY, train=True, batch_size=256):
	"""
	:param train: train or test fold?
	:param batch_size: batch size, int
	:return: CIFAR10 loader
	"""	
	transform = transforms.Compose([transforms.ToTensor(),transforms.Normalize((.5,.5,.5),(.5,.5,.5))])
	if train:
		data_set = CIFARIMAGEDATASET(trainX,trainY,transform = transform)
	else:
		data_set = CIFARIMAGEDATASET(testX, testY, transform = transform)
	loader = torch.utils.data.DataLoader(data_set, batch_size=batch_size,
									 shuffle=train, num_workers=4)
	return loader


def calc_accuracy(model, loader, verbose=False):
    """
    :param model: model network
    :param loader: torch.utils.data.DataLoader
    :param verbose: show progress bar, bool
    :return accuracy, float
    """
    mode_saved = model.training
    model.train(False)
    use_cuda = torch.cuda.is_available()
    if use_cuda:
        model.cuda()
    outputs_full = []
    labels_full = []
    for batch in tqdm(iter(loader), desc="Full forward pass", total=len(loader), disable=not verbose):
        inputs, labels = batch["image"], batch["label"]
        if use_cuda:
            inputs = inputs.cuda()
            labels = labels.cuda()
        with torch.no_grad():
            outputs_batch = model(inputs)
        outputs_full.append(outputs_batch)
        labels_full.append(labels)
    model.train(mode_saved)
    outputs_full = torch.cat(outputs_full, dim=0)
    labels_full = torch.cat(labels_full, dim=0)
    _, labels_predicted = torch.max(outputs_full.data, dim=1)
    accuracy = torch.sum(labels_full == labels_predicted).item() / float(len(labels_full))
    return accuracy
