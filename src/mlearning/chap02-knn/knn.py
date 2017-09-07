#-*- coding: UTF-8 -*-
from numpy import *
import operator

def classifyPerson():
	resultList = ['not at all','in small doses','in large doses']
	percentTats = float(raw_input("percentage of time spent playing video games?"))
	ffMiles = float(raw_input("frequent filter miles earned per year?"))
	iceCream = float(raw_input("liters of ice cream consumed per year?"))
	datingDataMat,datingLables = file2matrix('datingTestSet2.txt')
	normMat,ranges,minVals = autoNorm(datingDataMat)
	inArr = array([ffMiles,percentTats,iceCream])
	classifierResult = classify0((inArr-minVals)/ranges,normMat,datingLables,3)
	print "You will probably like this person:", resultList[classifierResult-1]

def datingClassTest():
	hoRatio = 0.10
	datingDataMat,datingLabels = file2matrix('datingTestSet2.txt')
	normMat,ranges,minVals = autoNorm(datingDataMat)
	m = normMat.shape[0]
	numTestVecs = int(m*hoRatio)
	errorCount = 0.0
	for i in range(numTestVecs):
		classifierResult = classify0(normMat[i,:],normMat[numTestVecs:m,:],datingLabels[numTestVecs:m],3)
		print "the classifier came back with: %d, the real answer is: %d" %(classifierResult,datingLabels[i])

		if(classifierResult != datingLabels[i]) : errorCount+=1.0

	print "total error rate is : %f " %(errorCount/float(numTestVecs))


def autoNorm(dataSet):
	minValue = dataSet.min(0) # 寻找最小值
	maxValue = dataSet.max(0) # 寻找最大值
	ranges = maxValue - minValue # 最大值-最小值
	normDataSet = zeros(shape(dataSet))
	m = dataSet.shape[0]
	normDataSet = dataSet - tile(minValue,(m,1))
	normDataSet = normDataSet/tile(ranges,(m,1)) # 值 - 最小值 ／ 最大值 - 最小值
	return normDataSet, ranges, minValue

def file2matrix(filename):
	fr = open(filename)
	arrayOLines = fr.readlines()
	numberOfLines = len(arrayOLines) # 获得总的记录条数
	returnMat = zeros((numberOfLines,3)) # 初始化矩阵，全都置为0
	classLabelVector = []
	index = 0
	for line in arrayOLines:
		line = line.strip()
		listFromLine = line.split('\t')
		returnMat[index,:] = listFromLine[0:3]
		classLabelVector.append(int(listFromLine[-1]))
		index += 1

	# returnMat 返回全部的值
	# classLabelVector 数据对应的标签
	return returnMat,classLabelVector


def createDataSet():
	group = array([[1.0,1.1],[1.0,1.0],[0,0],[0,0.1]])
	labels = ['A','A','B','B']
	return group,labels

def classify0(inX, dataSet, labels, k):
	# 获取数据集的大小， 4
	dataSetSize = dataSet.shape[0]

	# 复制输入的向量，然后做减法
	diffMat = tile(inX, (dataSetSize,1)) - dataSet
	# print diffMat
	sqDiffMat = diffMat**2
	sqDistances = sqDiffMat.sum(axis=1)
	distances = sqDistances**0.5
	sortedDistIndices = distances.argsort()
	classCount = {}
	for i in range(k):
		voteIlable = labels[sortedDistIndices[i]]
		classCount[voteIlable] = classCount.get(voteIlable,0)+1
	sortedClassCount = sorted(classCount.iteritems(),key=operator.itemgetter(1),reverse=True)
	return sortedClassCount[0][0]
