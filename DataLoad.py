import os
import numpy as np

def unpickle(file):
	import pickle
	with open(os.path.join(os.path.join(os.getcwd(),'Data'),file), 'rb') as fo:
		dict = pickle.load(fo, encoding='bytes')
	return dict

def Data():
	Dictionary1 = unpickle("data_batch_1")
	Dictionary2 = unpickle("data_batch_2")
	Dictionary3 = unpickle("data_batch_3")
	Dictionary4 = unpickle("data_batch_4")
	Dictionary5 = unpickle("data_batch_5")
	LabelDictionary = unpickle("batches.meta")
	Batch = [Dictionary1[b'data'], Dictionary2[b'data'],Dictionary3[b'data'],
	Dictionary4[b'data'],Dictionary5[b'data']]
	Labels = [Dictionary1[b'labels'], Dictionary2[b'labels'],Dictionary3[b'labels'],
	Dictionary4[b'labels'],Dictionary5[b'labels']]
	LabelNames = LabelDictionary[b'label_names']
	return Batch, Labels, LabelNames

