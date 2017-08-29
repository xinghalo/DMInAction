#-*- coding: UTF-8 -*-
from numpy import *
import operator

def createDataSet():
	group = array([[1.0,1.1],[1.0,1.0],[0,0],[0,0.1]])
	labels = ['A','A','B','B']
	return group,labels

def classify0(inX, dataSet, labels, k):
	# 获取数据集的大小， 4
	dataSetSize = dataSet.shape[0]

	diffMat = tile(inX, (dataSetSize,1)) - dataSet
	print diffMat
	sqDiffMat = diffMat**2
	print sqDiffMat
	sqDistances = sqDiffMat.sum(axis=1)
	distances = sqDistances**0.5
	print distances
	sortedDistIndices = distances.argsort()
	print sortedDistIndices
	classCount = {}
	for i in range(k):
		voteIlable = labels[sortedDistIndices[i]]
		classCount[voteIlable] = classCount.get(voteIlable,0)+1
	sortedClassCount = sorted(classCount.iteritems(),key=operator.itemgetter(1),reverse=True)
	return sortedClassCount[0][0]
