#this script parses the log file into a list and calibrates the values
#David Banville 14-06-2017

#TODO:
# 1) Average the 5 readings before saving (done)
# 2) write also rh to file (done)
# 3) write a time stamp to file (done)
# 4) write a linux script to create one file for each day
# 5) setup a cron task to stop and execute the script every day

#Import libraries
import numpy as np

#Open up the file and strip it (remove all the /n 's)
filename = "13-07-17-11-23.txt"
f = open(filename)
content = f.readlines()
content = [x.strip() for x in content]

timestamps = content[0:len(content):7]
readings = content[5:len(content):7]

#average temperature readings
temp = []
relhum = []
relhum_tcomp = []
time = []
rawhum = []
adcvalues = []

for i in range(0, len(readings)):
    T_sum = 0
    SORH_sum = 0
    RHlin_sum = 0
    RHtrue_sum = 0
    adc_sum = 0
    

    #extract time stamp
    time.append(int(timestamps[i][0:-27], 10))
    sparsed_reading = readings[i][10:-2].split(" ")
    
    #extract and convert temperature values

    
    for j in range(1, len(sparsed_reading), 3):
        
        T = int(sparsed_reading[j], 16) * 0.01 - 39.6
        #T = int(sparsed_reading[j], 16)
        T_sum += T
        
        #
        if j == 7:
        
            temp.append(T_sum / 3)
            #reset the summed readings
            T_sum = 0

    #extract and convert relative humidity values
    for j in range(2, len(sparsed_reading), 3):
        
        SORH = int(sparsed_reading[j], 16)
        RH_lin = pow(SORH, 2) * -1.5955e-6 + SORH * 0.0367 - 2.0468
        RH_true = (temp[i] - 25) * (0.01 + SORH * 0.00008) + RH_lin
        RHlin_sum += RH_lin
        RHtrue_sum += RH_true
        SORH_sum += SORH

        #if index-19 divisible by 4
        if j == 8:
        
            relhum.append(RHlin_sum / 3)
            relhum_tcomp.append(RHtrue_sum / 3)
            rawhum.append(SORH_sum / 3)

            #reset the summed readings
            RHlin_sum = 0
            RHtrue_sum = 0
            SORH_sum = 0

    for j in range(0, len(sparsed_reading), 3):

        adc = int(sparsed_reading[j], 16) * 1500 / 4096
        adc_sum += adc

        #
        if j == 6:
            adcvalues.append(adc_sum / 3)
            # reset the summed readings
            adc_sum = 0

interval = []
for i in range(0, len(time)-1):
    interval.append(time[i+1]-time[i])
        
#Write values to a csv file
p = open(filename[:-4] + ".csv", 'w')
l = [range(1,len(readings)+1), time, temp, relhum_tcomp, adcvalues]
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



