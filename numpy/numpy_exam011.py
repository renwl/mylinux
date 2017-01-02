#coding=utf-8
"""
numpy基本功能学习继续
"""
import numpy as np
#Print the minimum and maximum representable value for each numpy scalar type (★★☆)
print("*-"*40)
print("Print the minimum and maximum representable value for each numpy scalar type (★★☆)")
for dtype in [np.int8, np.int32, np.int64]:
   print("min=",np.iinfo(dtype).min)
   print("max=",np.iinfo(dtype).max)
print("x"*40)
for dtype in [np.float32, np.float64]:
   print("min=",np.finfo(dtype).min)
   print("max=",np.finfo(dtype).max)
   print("eps=",np.finfo(dtype).eps)

#How to print all the values of an array? (★★☆)
print("*-"*40)
print("How to print all the values of an array? (★★☆)")
np.set_printoptions(threshold=np.nan)
Z = np.zeros((16,16))
print(Z)

#How to find the closest value (to a given scalar) in an array? (★★☆)
print("*-"*40)
print("How to find the closest value (to a given scalar) in an array? (★★☆)")
Z = np.arange(100)
v = np.random.uniform(0,100)
index = (np.abs(Z-v)).argmin()
print(Z[index])

