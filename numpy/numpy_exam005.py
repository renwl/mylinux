#coding=utf-8
"""
numpy基本功能学习继续
"""
import numpy as np
print("*-"*40)
print("reverse vector")
z=np.arange(50)
print("z=",z)
z=z[::-1]
print("reverse z=",z)
#Find indices of non-zero elements from [1,2,0,0,4,0]
print("*-"*40)
print("Find indices of non-zero elements")
nz = np.nonzero([1,2,0,0,4,0])
print(nz)
#Create a 3x3 identity matrix
print("*-"*40)
print("Create a 3x3 identity matrix")
Z = np.eye(3)
print(Z)
#Create a 3x3x3 array with random values 
print("*-"*40)
print("Create a 3x3x3 array with random values")
Z = np.random.random((3,3,3))
print(Z)
#Create a 10x10 array with random values and find the minimum and maximum values
print("*-"*40)
print("Create a 10x10 array with random values and find the minimum and maximum values")
Z = np.random.random((10,10))
print(Z)
Zmin, Zmax = Z.min(), Z.max()
print(Zmin, Zmax)
#Create a random vector of size 30 and find the mean value (★☆☆)
print("*-"*40)
print("Create a random vector of size 30 and find the mean value")
Z = np.random.random(30)
print(Z)
m = Z.mean()
print(m)
#Create a 2d array with 1 on the border and 0 inside (★☆☆)
print("*-"*40)
print("Create a 2d array with 1 on the border and 0 inside★☆☆")
Z = np.ones((10,10))
Z[1:-1,1:-1] = 0
print(Z)
#How to add a border (filled with 0's) around an existing array? (★☆☆)
print("*-"*40)
print(r"How to add a border (filled with 0's) around an existing array? (★☆☆)")
Z = np.ones((5,5))
print(Z)
Z = np.pad(Z, pad_width=1, mode='constant', constant_values=0)
print(Z)

