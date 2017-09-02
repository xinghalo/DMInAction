import knn

datingDataMat,datingLabels = knn.file2matrix('datingTestSet2.txt')
normMat,ranges,minVals = knn.autoNorm(datingDataMat)

print normMat
print ranges
print minVals