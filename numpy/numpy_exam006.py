#coding=utf-8
"""
numpy基本功能学习继续
"""
import numpy as np
print("*-"*40)
print("numpy中的不等式")
#What is the result of the following expression? (★☆☆)
print(0 * np.nan)
print(np.nan == np.nan)
print(np.inf > np.nan)
print(np.nan - np.nan)
print(0.3 == 3 * 0.1)
#Create a 5x5 matrix with values 1,2,3,4 just below the diagonal (★☆☆)
print("*-"*40)
print("Create a 5x5 matrix with values 1,2,3,4 just below the diagonal (★☆☆)")
Z = np.diag(1+np.arange(4),k=-1)
#Z = np.diag(1+np.arange(4),k=2)
print(Z)
#Create a 8x8 matrix and fill it with a checkerboard pattern (★☆☆)
print("*-"*40)
print("Create a 8x8 matrix and fill it with a checkerboard pattern (★☆☆)")
Z = np.zeros((8,8),dtype=int)
print(Z)
Z[1::2,::2] = 1
Z[::2,1::2] = 1
print(Z)
#Consider a (6,7,8) shape array, what is the index (x,y,z) of the 100th element?
print("*-"*40)
print("Consider a (6,7,8) shape array, what is the index (x,y,z) of the 100th element?")
print(np.unravel_index(100,(6,7,8)))
#Create a checkerboard 8x8 matrix using the tile function (★☆☆)
print("*-"*40)
print("Create a checkerboard 8x8 matrix using the tile function (★☆☆)")
Z = np.tile( np.array([[0,1],[1,0]]), (4,4))
print(Z)
#Normalize a 5x5 random matrix (★☆☆)
print("*-"*40)
print("Normalize a 5x5 random matrix (★☆☆)")
Z = np.random.random((5,5))
print(Z)
Zmax, Zmin = Z.max(), Z.min()
Z = (Z - Zmin)/(Zmax - Zmin)
print(Z)