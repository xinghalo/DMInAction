import trees

myDat,labels  = trees.createDataSet()
print myDat

print trees.calcShannonEnt(myDat)

'''
myDat[0][-1] = 'maybe'

print trees.calcShannonEnt(myDat)

arr = [1,2,3,4,5,6]
print arr[1:]
print arr[:3]

print trees.splitDataSet(myDat,1,1)
print trees.splitDataSet(myDat,0,0)
'''

print trees.chooseBestFeautreToSplit(myDat)
