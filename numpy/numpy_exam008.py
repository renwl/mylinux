#coding=utf-8
"""
numpy基本功能学习继续
"""
#What is the output of the following script? (★☆☆)
# Author: Jake VanderPlas
print("*-"*40)
print("What is the output of the following script?")
x=list(range(5))
print(x)
print(sum(range(5),-1))
from numpy import *
x=list(range(5))
print(x)
print(sum(range(5),-1))
#How to round away from zero a float array ? (★☆☆)

# Author: Charles R Harris
import numpy as np
print("*-"*40)
print("How to round away from zero a float array ? (★☆☆)")

Z = np.random.uniform(-10,+10,10)
print(Z)
print (np.copysign(np.ceil(np.abs(Z)), Z))

#How to find common values between two arrays? (★☆☆)
print("*-"*40)
print("How to find common values between two arrays? (★☆☆)")
Z1 = np.random.randint(0,10,10)
Z2 = np.random.randint(0,10,10)
print(Z1)
print(Z2)
print(np.intersect1d(Z1,Z2))

#How to ignore all numpy warnings (not recommended)? (★☆☆)
# Suicide mode on

defaults = np.seterr(all="ignore")
Z = np.ones(1) / 0
# Back to sanity
_ = np.seterr(**defaults)
#An equivalent way, with a context manager:
with np.errstate(divide='ignore'):
    Z = np.ones(1) / 0