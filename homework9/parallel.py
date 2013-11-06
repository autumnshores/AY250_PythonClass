from random import uniform
from math import sqrt
from time import time


### Serial processing

#specify number of darts with which to run simulation
numdarts = [range(10,100), range(100,1000,10), range(1000,10000,100), range(10000,100000,1000), range(100000,1000000,10000), range(1000000,10100000,100000)]
#execution time array for plotting
extime_serial= []
#simulation rate array for plotting
simrate_serial = []
count = 0

#the code (given)
for moo in numdarts:
    for number_of_darts in moo:
        number_of_darts_in_circle = 0

        start_time = time()

        for n in range(number_of_darts):
            x,y = uniform(0,1), uniform(0,1)
            if sqrt((x - 0.5)**2 + (y - 0.5)**2) <= 0.5:
                number_of_darts_in_circle += 1

        end_time = time()
        execution_time = end_time - start_time
        extime_serial.append(execution_time)
        simrate_serial.append(number_of_darts/execution_time)

        pi_approx = 4 *number_of_darts_in_circle / float(number_of_darts)
        count += 1

        print "Pi Approximation:", pi_approx
        print "Number of Darts:", number_of_darts
        print "Execution Time (s):", execution_time
        print "Darts Thrown per Second:", number_of_darts/execution_time
        print "Count:", count



### Multiprocessing

from multiprocessing import Pool

def f(numdarts):
    extime_mp = []
    simrate_mp = []
    count = 0
    for moo in numdarts:
        for number_of_darts in moo:
            number_of_darts_in_circle = 0
        
            start_time = time()
        
            for n in range(number_of_darts):
                x,y = uniform(0,1), uniform(0,1)
                if sqrt((x - 0.5)**2 + (y - 0.5)**2) <= 0.5:
                    number_of_darts_in_circle += 1
        
            end_time = time()
            execution_time = end_time - start_time
            extime_mp.append(execution_time)
            simrate_mp.append(number_of_darts/execution_time)
        
            pi_approx = 4 *number_of_darts_in_circle / float(number_of_darts)
            count += 1
        
            print "Pi Approximation:", pi_approx
            print "Number of Darts:", number_of_darts
            print "Execution Time (s):", execution_time
            print "Darts Thrown per Second:", number_of_darts/execution_time
            print "Count:", count
    return extime_mp, simrate_mp


if __name__ == '__main__':
    pool = Pool(processes=4)
    test = pool.map(f, [numdarts])

extime_mp = test[0][0]
simrate_mp = test[0][1]



### IPython Parallel

from IPython import parallel
rc = parallel.Client()

def f(numdarts):
    extime_parallel=[]
    simrate_parallel=[]
    count = 0
    for moo in numdarts:
        for number_of_darts in moo:
            number_of_darts_in_circle = 0
            
            start_time = time()
            
            for n in range(number_of_darts):
                x,y = uniform(0,1), uniform(0,1)
                if sqrt((x - 0.5)**2 + (y - 0.5)**2) <= 0.5:
                    number_of_darts_in_circle += 1
            
            end_time = time()
            execution_time = end_time - start_time
            extime_parallel.append(execution_time)
            simrate_parallel.append(number_of_darts/execution_time)
            
            pi_approx = 4 *number_of_darts_in_circle / float(number_of_darts)
            count += 1
            
            print "Pi Approximation:", pi_approx
            print "Number of Darts:", number_of_darts
            print "Execution Time (s):", execution_time
            print "Darts Thrown per Second:", number_of_darts/execution_time
            print "Count:", count
    return extime_parallel, simrate_parallel

view = rc.load_balanced_view()
test2 = view.map(f, [numdarts])

extime_parallel = test2[0][0]
simrate_parallel = test2[0][1]



### now start plotting
%pylab
import matplotlib.pyplot as plt
import numpy as np

#create xaxis array
xaxis = []
for i in numdarts:
    for j in i:
        xaxis.append(j)

#plot execution time on left axis for serial
f1, axL = plt.subplots()
line1 = axL.plot(xaxis, extime_serial,label='Serial',linewidth=2,color='r')
axL.minorticks_on()
axL.set_xscale('log')
axL.set_yscale('log')
axL.set_xlabel('Darts Thrown')
axL.set_ylabel('Execution Time (seconds), solid line')
axL.legend(loc='top left',fontsize='10')

#add multiprocessing plot
line2 = axL.plot(xaxis, extime_mp,label='Multiprocessing',linewidth=2,color='c')

#add parallel plot
#line3 = axL.plot(xaxis, extime_parallel,label='IPcluster',linewidth=2,color='g')

#add second axis for simulation rate, serial
axR = axL.twinx()
line4 = axR.plot(xaxis, simrate_serial,linewidth=2,linestyle='--',color='r')
axR.minorticks_on()
axR.set_ylabel('Simulation Rate (darts/second), dashed line')
axL.set_yscale('log')

#add multiprocessing plot
line5 = axR.plot(xaxis, simrate_mp,linewidth=2,linestyle='--',color='c')

#add parallel plot
#line6 = axR.plot(xaxis, simrate_parallel,linewidth=2,linestyle='--',color='g')

#save figure
plt.show()
savefig('parallel.png')
