import knn
group,labels = knn.createDataSet()
# print labels

print knn.classify0([0, 0], group, labels, 3)