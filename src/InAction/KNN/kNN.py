#-*- coding: UTF-8 -*- 
from numpy import * #导入numpy
import operator #导入运算符包

# 创建数据集
def createDataSet():
	group = array([[1.0,1.1],[1.0,1.0],[0,0],[0,0.1]])
	labels = ['A','A','B','B']
	return group,labels

def classify0(inX,dataSet,labels,k):
	dataSetSize = dataSet.shape[0] # 数据的大小
	diffMat = tile(inX,(dataSetSize,1)) - dataSet # tile方法再行上重复dataSetSize，在列上重复1次，重复的是inX
	sqDiffMat = diffMat**2
	sqDistances = sqDiffMat.sum(axis=1)
	distances = sqDistances**0.5
	sortedDisIndices = distances.argsort()
	classCount = {}
	for i in range(k):
		voteIlabel = labels[sortedDisIndices[i]]
		classCount[voteIlabel] = classCount.get(voteIlabel,0)+1
	sortedClassCount = sorted(classCount.iteritems(),key=operator.itemgetter(1),reverse=True)
	return sortedClassCount[0][0]