#!/usr/bin/python
import matplotlib.pyplot as plt

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


