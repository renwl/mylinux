#coding=utf-8
"""
numpy基本功能学习继续
"""
import numpy as np
#Create a custom dtype that describes a color as four unisgned bytes (RGBA) (★☆☆)
print("*-"*40)
print("Create a custom dtype that describes a color as four unisgned bytes (RGBA) (★☆☆)")
color = np.dtype([("r", np.ubyte, 1),
                  ("g", np.ubyte, 1),
                  ("b", np.ubyte, 1),
                  ("a", np.ubyte, 1)])
print(color)
#Multiply a 5x3 matrix by a 3x2 matrix (real matrix product) (★☆☆)
print("*-"*40)
print("Multiply a 5x3 matrix by a 3x2 matrix (real matrix product) (★☆☆)")
Z = np.dot(np.ones((5,3)), np.ones((3,2)))
print(Z)

# Alternative solution, in Python 3.5 and above
Z = np.ones((5,3)) @ np.ones((3,2))
print(Z)
#Given a 1D array, negate all elements which are between 3 and 8, in place. (★☆☆)
# Author: Evgeni Burovski
print("*-"*40)
print("Given a 1D array, negate all elements which are between 3 and 8, in place. (★☆☆)")
Z = np.arange(11)
Z[(3 < Z) & (Z <= 8)] *= -1
print(Z)