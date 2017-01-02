#coding=utf-8
"""
numpy官网快速教程
基础：
NumPy的主要对象是同一类型的多维数组。 它是一个元素（通常是数字）的表，
所有类型都由正整数的元组索引。在Numpy中维度称为轴。 轴数为rank。

例如，3D空间[1,2,1]中的点的坐标是rank 1的数组，因为它具有一个轴。 
该轴的长度为3.在下图所示的示例中，数组具有rank 2（它是2维的）。 
第一维度（轴）的长度为2，第二维度的长度为3。
[[ 1., 0., 0.],
 [ 0., 1., 2.]]
Numpy的数组类称为ndarray。 它的别名数组被人所熟知。 请注意，
numpy.array与标准Python库类array.array不同，后者仅处理
一维数组并提供较少的功能。 一个ndarray对象的更重要的属性是：
ndarray.ndim
    数组的轴数（维数）。在Python世界中，维度的数量被称为rank。
ndarray.shape
    数组的维数。这是一个整数的元组，表示每个维度中数组的大小。
    对于具有n行和m列的矩阵，形状将是（n，m）。因此，形状元组
    的长度是rank或维度数目ndim。
ndarray.size
    数组元素的总数。这等于形状元素的乘积。
ndarray.dtype
    描述数组中元素类型的对象。可以使用标准Python类型创建或指
    定dtype。另外NumPy提供自己的类型。 numpy.int32，numpy.int16
    和numpy.float64是一些示例。
ndarray.itemsize
    数组中每个元素的字节大小。例如，float64类型的元素数组具有项目
    大小8（= 64/8），而类型complex32中的一个具有项目大小4（= 32/8）。
    它等同于ndarray.dtype.itemsize。
ndarray.data
    该缓冲区包含数组的实际元素。通常，我们不需要使用此属性，
    因为我们将使用索引访问数组中的元素。
"""
#实际列子
import numpy as np
print("*-"*40)
a = np.arange(15).reshape(3, 5)
print("a=",a)
print("a.shape=",a.shape)
print("a.ndim=",a.ndim)
print("a.dtype.name=",a.dtype.name)
print("a.itemsize=",a.itemsize)
print("a.size=",a.size)
print("type(a)=",type(a))
b = np.array([6, 7, 8])
print("b=",b)
print("type(b)=",type(b))
#常见的错误包括调用具有多个数字参数的数组，
#而不是提供单个数字列表作为参数。
# a = np.array(1,2,3,4)    # WRONG
# a = np.array([1,2,3,4])  # RIGHT
#array将序列的序列转换成二维阵列，将序列的序列的序列
#转换成三维阵列，等等。
b = np.array([(1.5,2,3), (4,5,6)])
print("序列的序列=",b)
#数组的类型也可以在创建时明确指定：
print("*-"*40)
c = np.array( [ [1,2], [3,4] ], dtype=complex )
print("c=",c)
#通常，数组的内容最初是未知的，但其大小是已知的。 
#因此，NumPy提供了几个函数来创建具有初始占位符内容的数组。 
#这些最小化了阵列长度可变的必要性，这是一种昂贵的操作。
#函数零创建一个由零组成的数组，函数1创建一个由1组成的数组，
#函数empty创建一个数组，其初始内容是随机的，取决于内存的状态。 
#默认情况下，创建的数组的dtype为float64。
x=np.zeros( (3,4) )
print(x)
y=np.ones( (2,3,4), dtype=np.int16 )
print(y)
z=np.empty( (2,3) )
print(z)

#为了创建数字阵列，NumPy提供了一个类似于范围的函数，返回数组而不是列表
x=np.arange( 10, 30, 5 )
print("arange阵列:	",x)
y= np.arange( 0, 2, 0.3 ) 
print("arange阵列:	",y)
#当arange使用浮点参数的范围时，由于有限的浮点精度，通常不可能预测获得的元素
#的数量。 出于这个原因，通常最好使用函数linspace，它接收我们想要的元素
#数量作为参数，而不是步骤：
x=np.linspace( 0, 2, 9 )  
print("x=",x)
from numpy import pi
x = np.linspace( 0, 2*pi, 100 ) 
f = np.sin(x)
print("np.sin(x)=",f)