import numpy as np
import matplotlib.pyplot as plt
print "0"

plt.figure(1)
ax1=plt.subplot(211)
x=np.linspace(0,100,100)
for i in xrange(1,100):
	plt.figure(1)
	plt.plot(x,x*2)
plt.show()