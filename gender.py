# -*- coding: utf-8 -*-
"""
Created on Fri Jul 06 20:49:18 2018

@author: ASHISH
"""

import numpy
import random
from sklearn import svm

f = open("wiki5.csv","r");
array = f.readlines()
array = array[1:]

dataset = list()

for x in array :
    dataset.append(list())
    for y in x.split(","):
        dataset[len(dataset)-1].append(int(y))
        
   

labels = list()

for data in dataset:
    labels.append(data[1])

image_dataset = []

for data in dataset:
    image_dataset.append(numpy.asarray(data[3:]))
    
train_data = image_dataset[0:2500]
train_labels = labels[0:2500]

test_data = image_dataset[2200:3200]
test_labels = labels[2200:3200]

classify = svm.SVC(kernel="poly")
classify.fit(train_data, train_labels)

pred = classify.predict(test_data)

  
total = 0

for i in range(0, pred.shape[0]):
    if pred[i] == test_labels[i]:
        total = total +1
        
percentage = (total *1.0)/pred.shape[0] * 100

print percentage

     

    
    