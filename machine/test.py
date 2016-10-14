from machine.knn import *
from numpy import *

dataSet, labels = createDataSet()

testX = array([1.2, 1.0])
k = 3
outputLabel = kNNClassify(testX, dataSet, labels, 3)
print ("Your input is:", testX, "and classified to class: ", outputLabel)

testX = array([0.1, 0.3])
outputLabel = kNNClassify(testX, dataSet, labels, 3)
print ("Your input is:", testX, "and classified to class: ", outputLabel  )