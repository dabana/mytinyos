

import matplotlib.pyplot as plt
import pylab
import numpy as np

a = pylab.loadtxt("17-07-17-15-55_MgSSf1.csv", delimiter=",")

time_secs = (a[:, 1] - a[0, 1]) / 1000
time_mins = time_secs / 60
time_hs = time_mins / 60
diff_time_sec = (a[1:, 1] - a[0:-1, 1]) / 1000

filt_diff_t = np.zeros((1, 1))
filt_t = np.zeros((1, 1))

for i in range(0, len(diff_time_sec)):
    # if i == 0:
    #     filt_diff_t = np.ones(1) * diff_time_sec[i]
    #     filt_t = np.ones(1) * time_hs[i]
    if 50 > diff_time_sec[i] > 0.1:
        filt_diff_t = np.append(filt_diff_t, diff_time_sec[i])
        filt_t = np.append(filt_t, time_hs[i])

#Convert discharge time to current

current = 1.06 * 2 * 470e-6 / filt_diff_t

plt.plot(time_hs, a[:, 2], "k.")
plt.show()
plt.plot(filt_t, current, "k.")
plt.show()

