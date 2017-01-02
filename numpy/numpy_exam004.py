#coding=utf-8
"""
numpy的基本用法说明，实例。
"""
import numpy as np
import pylab as pl
print(np.__version__)
np.show_config()
print("*-"*40)
print("计算python的list大小")
x=[1,2]
y=[[4,1],[2,2]]
#print("x's size=",x.size)
#print("y's size=",y.size)
print("np.dot=",np.dot(x,y))
print("np.dot=",np.dot(y,x))
print("*-"*40)
print("计算numpy的array大小")
x=np.array([1,2])
y=np.array([[4,1],[2,2]])
print("x's size=",x.size)
print("y's size=",y.size)
print("x's single number mem size=",x.itemsize)
print("y's single number mem size=",y.itemsize)
print("x's mem size=%d bytes"%(x.size * x.itemsize))
print("y's mem size=%d bytes"%(y.size * y.itemsize))
print("np.dot(x,y)=",np.dot(x,y))
print("np.dot(y,x)=",np.dot(y,x))
print("*-"*40)
#numpy自己创造array
print("numpy自己创造array实例")
z=np.zeros(10)
z[4]=1
print(z)
z=z.reshape(5,2)
print(z)
z=np.zeros((10,10))
print(z)
z=np.arange(10,50)
print(z)
#numpy函数查看
print("numpy函数查看")
np.info(np.add)

      
