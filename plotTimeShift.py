#!/usr/bin/python
import matplotlib.pyplot as plt
import numpy as np
from math import log
x = []
y = []

xDer = []
yDer = []

f = open('timeCorrection2.txt')
f.readline()

for line in f.readlines():
    lineArray = line.split()
    x.append(float(lineArray[0]))
    y.append(float(lineArray[1]))

for i in range(0,len(x) - 1):
	xDer.append((x[i] + x[i+1])/2.)
	yDer.append((y[i+1] -y[i])/(x[i+1] - x[i]))

plt.plot(x,y,'s-',color='#00549F',label='time shift')
plt.axis([0.45,1.55,-6,26])
plt.xlabel('weighted bin position')
plt.ylabel('time shift / ns')
plt.title('Time shift for position of maximum')
#plt.savefig('timeShift.png')
plt.show()

def f(x):  
  return np.min([6,9.28 - 2.06*log(x)])
 
vectorizedFun = np.vectorize(f)

x = np.linspace(0.1,60,100)
y = vectorizedFun(x)

fig = plt.figure()
plt.plot(x,y)
plt.xlabel('charge / fC')
plt.ylabel('time slew / ns')
plt.title('time slew vs. charge')
plt.axis([0,60,0,6.5])
plt.show()