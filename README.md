# CS220-Graph-Learning

This repository contains a high-level introduction on the types of prediction problems that two common Graph Neural Network architectures may be applied on, as well as example implementations demonstrating end-to-end training pipelines, serving as a starting point for various prediction applications. In addition, there is a small primer on computing with tensors, which are multidimensional array representations of data that enable optimized operations in common machine learning frameworks.

## Graph Convolutional Networks (GCN) 
GCNs are applied to problems where, given a graph with vertex and/or edge attributes, the objective is to predict some quantity at one or more individual vertices, or even a single global quantity, describing the graph. 

For example, let the undirected graph below represent a small social network between five individuals, each with some attributes or features denoted by the vectors. These features may be any data we have that may be relevant (e.g. number of followers, posting frequency, etc.) We may be interested in vertex-level predictions, like ‘whether or not a given person is invited to an event hosted by person 1’. Alternatively, we may be interested in global or graph-level predictions, e.g. ‘is this network one between students? Professionals?’ From hereon, we will focus on vertex-level predictions.

<p align="center">
  <img src="https://i.imgur.com/AXKuITH.png" />
</p>

### Tutorial and example code 
The Deep Graph Library documentation provides a concise tutorial on GCN training at https://docs.dgl.ai/tutorials/blitz/1_introduction.html. It provides an example implementation of a GCN for classifying the domain of publications in a citation network, as well as a minimal end-to-end GCN training pipeline. This code is also in this repository (**GCN_Cora.py**).

The dataset is automatically downloaded when executing the example code, and the python file can simply be executed with python 3, without any arguments. If using the code supplied in this repository (recommended) setting the **USE_GPU** flag in the 'main' block specifies whether or not the model will be trained on GPU, instead of CPU. 

## Message-Passing Graph Neural Networks (MPGNN)
Similar to GCNs, MPGNNs are capable of vertex-level and graph-level predictions. They are distinct, however, in that MPGNNs traverse the graph, computing values at vertices in order. There is an assumption of sequential dependence between vertices, contrasting with GCNs which don’t assume any ordering of vertices, and compute predictions on all of them simultaneously from their neighborhoods. For many problems, either architecture could be used, however, we need to draw upon domain knowledge to make these decisions intelligently.

For example, let’s assume the directed graph below represents a network of electric charging stations available to a next-generation autonomous semi truck on their delivery route, whose origin is at station 0. Each vertex, or charging station, has a corresponding feature vector denoted by x, representing some pertinent information (e.g. longitude/latitude, number of chargers, etc.) This time, edges also have features as well, denoted by the ‘w’ vectors, which might be attributes like weather, number of construction projects on the route, etc. After our vehicle has completed charging at a station, it only has sufficient charge to travel to those charging stations which are the sink vertices in any edge directed away from the current station. 

<p align="center">
  <img src="https://i.imgur.com/Xh6XLWS.png" />
</p>

On this graph, we may be interested in predicting the optimal route, with consideration to the charging station and route conditions. Since we must start at station 1, and end at station 4, and only one station may be visited at a time, MPGNNs would appear to be a suitable architecture for this prediction problem, since there is a natural ordering over nodes. In essence, the objective here is to predict the optimal path between stations 1 and 4, which may be formulated as a vertex-level prediction problem (is a given vertex on the optimal path?) 

<p align="center">
  <img src="https://i.imgur.com/e9TSUwr.png" />
</p>

### Tutorial and example code 
The Deep Graph Library provides a tutorial and example code for implementing a MPGNN for sentiment analysis, on tree-structured representations of language (https://docs.dgl.ai/en/0.4.x/tutorials/models/2_small_graph/3_tree-lstm.html). The prediction target in this example is the sentiment of subtrees in the graph, or whether they’re contributing a ‘positive’ or ‘negative’ view on the subjects in question. Similarly to the GCN example, the example code (named **MPGNN_SA.py** in this repository) downloads the dataset at execution, and executes an end-to-end training pipeline. The code may be executed with python 3, either with the argument **--gpu 0** if training on GPU is intended, or with no arguments, if the model is to be trained on CPU. *It is recommended that you use the code included in the repository, since some methods have been deprecated since the writing of the tutorial.* 

Though this architecture is dubbed the Tree LSTM, it is equivalently a particular case of the MPGNN, making predictions on tree-structured data (which are graphs!) The high-level concepts are exemplified in this example: there is a natural ordering of words, from lower-level grammatical objects, to those providing higher-level relationships between them, and information flows sequentially over this natural ordering when computing predictions.

## Tensor Operations
This section will soon be populated with a brief introduction on the basics of tensor operations, which are the building blocks of widely adopted deep learning frameworks.
