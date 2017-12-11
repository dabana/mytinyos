

import matplotlib.pyplot as plt
import pylab

a = pylab.loadtxt("04-07-17-13-41.csv", delimiter = ",")

time_secs = (a[:,1] - a[0,1]) / 1000
time_mins = time_secs / 60
time_hs = time_mins / 60

plt.plot(time_hs,a[:,2],"k.")
plt.plot(time_hs,a[:,4],"r.")
plt.show()
plt.plot(time_hs,a[:,3],"bo")
plt.show()
