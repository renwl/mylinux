#coding=utf-8
"""
numpy基本功能学习继续
"""
import numpy as np
#How to sum a small array faster than np.sum? (★★☆)
print("*-"*40)
print("How to sum a small array faster than np.sum? (★★☆)")
# Author: Evgeni Burovski
Z = np.arange(10)
print(np.add.reduce(Z))

#Consider two random array A anb B, check if they are equal (★★☆)
print("*-"*40)
print("Consider two random array A anb B, check if they are equal (★★☆)")
A = np.random.randint(0,2,5)
B = np.random.randint(0,2,5)
print("A=",A)
print("B=",B)
# Assuming identical shape of the arrays and a tolerance for the comparison of values
equal = np.allclose(A,B)
print(equal)
# Checking both the shape and the element values, no tolerance (values have to be exactly equal)
equal = np.array_equal(A,B)
print(equal)

#Make an array immutable (read-only) (★★☆)
print("*-"*40)
print("Make an array immutable (read-only) (★★☆)")
Z = np.zeros(10)
Z.flags.writeable = False
#Z[0] = 1
#print(Z)

#Consider a random 10x2 matrix representing cartesian coordinates, convert them to polar coordinates (★★☆)
print("*-"*40)
print("Consider a random 10x2 matrix representing cartesian coordinates, convert them to polar coordinates (★★☆)")
Z = np.random.random((10,2))
print("Z=",Z)
X,Y = Z[:,0], Z[:,1]
print("X=",X)
print("Y=",Y)
R = np.sqrt(X**2+Y**2)
T = np.arctan2(Y,X)
print("R=",R)
print("T=",T)

#Create random vector of size 10 and replace the maximum value by 0 (★★☆)
print("*-"*40)
print("Create random vector of size 10 and replace the maximum value by 0 (★★☆)")
Z = np.random.random(10)
print(Z)
Z[Z.argmax()] = 0
print(Z)

#Create a structured array with x and y coordinates covering the [0,1]x[0,1] area (★★☆)
print("*-"*40)
print("Create a structured array with x and y coordinates covering the [0,1]x[0,1] area (★★☆)")
Z = np.zeros((5,5), [('x',float),('y',float)])
Z['x'], Z['y'] = np.meshgrid(np.linspace(0,1,5),
                             np.linspace(0,1,5))
print(Z)

#Given two arrays, X and Y, construct the Cauchy matrix C (Cij =1/(xi - yj))

# Author: Evgeni Burovski
print("*-"*40)
print("Given two arrays, X and Y, construct the Cauchy matrix C (Cij =1/(xi - yj))")
X = np.arange(8)
Y = X + 0.5
C = 1.0 / np.subtract.outer(X, Y)
print("C=",C)
print(np.linalg.det(C))