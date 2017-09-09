import knn

testVector = knn.img2vector('data/test/0_13.txt')
print(testVector[0,0:31])
print(testVector[0,32:63])
knn.handwritingClassTest()