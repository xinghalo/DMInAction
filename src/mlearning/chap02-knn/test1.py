import knn
import matplotlib.pyplot as plt
import numpy as np

datingDataMat,datingLabels = knn.file2matrix('datingTestSet2.txt')

print datingDataMat
print datingLabels

fig = plt.figure()
ax = fig.add_subplot(111)
# ax.scatter(datingDataMat[:,1],datingDataMat[:,2])
ax.scatter(datingDataMat[:,1],datingDataMat[:,2],15.0*np.array(datingLabels),15.0*np.array(datingLabels))
plt.show()
