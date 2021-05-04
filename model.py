from DataLoad import Data
import numpy as np

Batches, Labels, LabelNames = Data()
print(Batches[0])
print(np.array(Labels[0]))
print(LabelNames)
