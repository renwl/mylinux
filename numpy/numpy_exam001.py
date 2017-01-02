#coding=utf-8
import numpy as np

import pylab as pl

 

# Use numpy to load the data contained in the file

# ’odom.txt’ into a 2-D array called data

data = np.loadtxt("odom.txt")

print(data[:,0]) 

# plot the first column as x, and second column as y

pl.plot(data[:,0], data[:,1],"ro")

pl.xlabel("x")

pl.ylabel("y")

pl.xlim(0.1,0.15)

pl.show()