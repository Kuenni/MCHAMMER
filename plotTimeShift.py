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

'''
raw delay = 23.97 - 3.18**log(x)
delay >= 0 && min(16,rawdelay)
'''

def f(x):  
  return np.min([6,9.28 - 2.06*log(x)])

def f2(x):
	if x < 1:
		x = 1
	rawDelay = 23.97 - 3.18*log(x)
	return 0 if rawDelay < 0 else (np.min([16,rawDelay]))
	
	
vectorizedFun = np.vectorize(f)
vectorizedFun2 = np.vectorize(f2)

x = np.linspace(0.1,60,100)
y = vectorizedFun(x)
y2 = vectorizedFun2(x)

fig = plt.figure()
plt.plot(x,y,color='#00549F',label='Time slew MC')
plt.plot(x,y2,color='#E30066',label='Time slew, 2nd function')
plt.legend()
plt.xlabel('charge / fC')
plt.ylabel('time slew / ns')
plt.title('time slew vs. charge')
plt.axis([0,60,0,16.5])
plt.show()