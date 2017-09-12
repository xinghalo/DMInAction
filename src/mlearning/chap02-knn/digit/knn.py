#-*- coding: UTF-8 -*-
from numpy import *
import operator
import os, sys

def handwritingClassTest():
	hwLabels = []
	trainingFileList = os.listdir('data/training')
	m = len(trainingFileList)
	trainingMat = zeros((m,1024))
	# 遍历每个文件，并且分析文件名字得到label
	for i in range(m):
		fileNameStr = trainingFileList[i]
		fileStr = fileNameStr.split('.')[0]
		classNumStr = int(fileStr.split('_')[0])
		hwLabels.append(classNumStr)
		trainingMat[i,:] = img2vector('data/training/%s' % fileNameStr)
	testFileList = os.listdir('data/test')
	errorCount = 0.0
	mTest = len(testFileList)
	for i in range(mTest):
		fileNameStr = testFileList[i]
		fileStr = fileNameStr.split('.')[0]
		classNumStr = int(fileStr.split('_')[0])
		vectorUnderTest = img2vector('data/test/%s' % fileNameStr)
		classifierResult = classify(vectorUnderTest,trainingMat,hwLabels,3)
		print("\ncame back with: %d, the real answer is: %d" % (classifierResult,classNumStr))
		if(classifierResult != classNumStr): errorCount += 1.0
	print("\nthe total number of errors is: %d" % errorCount)
	print("\nthe total error rate is : %f" % (errorCount/float(mTest)))

# 读取数据，并转换成一维向量
def img2vector(filename):
	returnVect = zeros((1,1024))
	fr = open(filename)
	for i in range(32):
		lineStr = fr.readline()
		for j in range(32):
			returnVect[0,32*i+j] = int(lineStr[j])
	return returnVect
def classify(inX, dataSet, labels, k):
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