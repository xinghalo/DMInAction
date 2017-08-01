import numpy as np
import matplotlib.pyplot as plt
plt.figure(1)
# ax1=plt.subplot(211)
x = np.linspace(-60,0,50) 
y = 2/(1+np.exp(-x-15))
for i in xrange(1,50):
	plt.figure(1)
	plt.plot(x,y)
plt.show()