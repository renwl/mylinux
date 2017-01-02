#coding=utf-8
"""
numpy基本功能学习继续
"""
import numpy as np
#Is the following expressions true? (★☆☆)
print("*-"*40)
print("Is the following expressions true? (★☆☆)")
print("np.sqrt(-1)=",np.sqrt(-1))
print("np.emath.sqrt(-1)=",np.emath.sqrt(-1))
np.sqrt(-1) == np.emath.sqrt(-1)

#How to get the dates of yesterday, today and tomorrow? (★☆☆)
print("*-"*40)
print("How to get the dates of yesterday, today and tomorrow? (★☆☆)")
yesterday = np.datetime64('today', 'D') - np.timedelta64(1, 'D')
today     = np.datetime64('today', 'D')
tomorrow  = np.datetime64('today', 'D') + np.timedelta64(1, 'D')
print("yesterday=",yesterday)
print("today=",today)
print("tomorrow=",tomorrow)

#How to get all the dates corresponding to the month of July 2016? (★★☆)
print("*-"*40)
print("How to get all the dates corresponding to the month of July 2016? (★★☆)")
Z = np.arange('2016-07', '2016-08', dtype='datetime64[D]')
print(Z)

#How to compute ((A+B)*(-A/2)) in place (without copy)? (★★☆)
print("*-"*40)
print("How to compute ((A+B)*(-A/2)) in place (without copy)? (★★☆)")
A = np.ones(3)*1
B = np.ones(3)*2
C = np.ones(3)*3
print("A=",A)
print("B=",B)
print("C=",C)
np.add(A,B,out=B)
np.divide(A,2,out=A)
np.negative(A,out=A)
np.multiply(A,B,out=A)
print("A=",A)

#Extract the integer part of a random array using 5 different methods (★★☆)
print("*-"*40)
print("Extract the integer part of a random array using 5 different methods (★★☆)")
Z = np.random.uniform(0,10,10)
print("Z=",Z)
print (Z - Z%1)
print (np.floor(Z))
print (np.ceil(Z)-1)
print (Z.astype(int))
print (np.trunc(Z))

#Create a 5x5 matrix with row values ranging from 0 to 4 (★★☆)
print("*-"*40)
print("Create a 5x5 matrix with row values ranging from 0 to 4 (★★☆)")
Z = np.zeros((5,5))
Z += np.arange(5)
print(Z)

#Consider a generator function that generates 10 integers and use it to build an array (★☆☆)
print("*-"*40)
print("Consider a generator function that generates 10 integers and use it to build an array (★☆☆)")
def generate():
    for x in range(10):
        yield x
Z = np.fromiter(generate(),dtype=float,count=-1)
print(Z)

#Create a vector of size 10 with values ranging from 0 to 1, both excluded (★★☆)
print("*-"*40)
print("Create a vector of size 10 with values ranging from 0 to 1, both excluded (★★☆)")
Z = np.linspace(0,1,12,endpoint=True)[1:-1]
#Z = np.linspace(0,1,12,endpoint=True)
print(Z)

#Create a random vector of size 10 and sort it (★★☆)
print("*-"*40)
print("Create a random vector of size 10 and sort it (★★☆)")
Z = np.random.random(10)
print(Z)
Z.sort()
print(Z)