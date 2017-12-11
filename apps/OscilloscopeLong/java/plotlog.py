

import matplotlib.pyplot as plt
import pylab

a = pylab.loadtxt("23-06-17-16-46.csv", delimiter = ",")

time_secs = (a[:,1] - a[0,1]) / 1000
time_mins = time_secs / 60
time_hs = time_mins / 60

plt.plot(time_hs,a[:,2],"k.")
plt.plot(time_hs,a[:,4],"bo")
plt.xlabel("Time (hours)")
plt.ylabel("Temperature (in degrees C) and relative humidity (%)")

plt.show()

