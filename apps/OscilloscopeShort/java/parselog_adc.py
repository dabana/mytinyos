#this script parses the log file into a list and calibrates the ADC values
#David Banville 14-07-2017

#Import libraries
import numpy as np

#Open up the file and strip it (remove all the /n 's)
filename = "17-07-17-15-55_MgSSf1.txt"
f = open(filename)
content = f.readlines()
content = [x.strip() for x in content]

timestamps = content[0:len(content):7]
readings = content[5:len(content):7]

#Harvest ADC readings and average them
#Harvest timestamp
time = []
adcvalues = []

for i in range(0, len(readings)):

    adc_sum = 0
    

    #extract time stamp
    time.append(int(timestamps[i][0:-27], 10))
    sparsed_reading = readings[i][10:-2].split(" ")


    for j in range(0, len(sparsed_reading)):

        adc = int(sparsed_reading[j], 16) * 1500 / 4096
        adc_sum += adc

        #
        if j == 1:
            adcvalues.append(adc_sum / 2)
            # reset the summed readings
            adc_sum = 0

interval = []
for i in range(0, len(time)-1):
    interval.append(time[i+1]-time[i])
        
#Write values to a csv file
p = open(filename[:-4] + ".csv", 'w')
l = [range(1,len(readings)+1), time, adcvalues]
l = np.asarray(l).T.tolist() #transpose the list
for row in l:
    cntr = 0
    for column in row:
        cntr += 1
        if cntr == len(row):
            p.write('%f' % column)
        else:
            p.write('%f,' % column)

    p.write('\n')
p.close()



