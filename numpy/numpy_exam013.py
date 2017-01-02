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
#数组上的算术运算符以元素方式应用。 将创建一个新数组并用结果填充。
a = np.array( [20,30,40,50] )
print("a=",a)
b=np.arange(4)
print("b=",b)
print("a-b=",a-b)
print("b**2=",b**2)
print("10*np.sin(a)=",10*np.sin(a))
print("a<35",a<35)
#与许多矩阵语言不同，乘法运算符*在NumPy数组中以元素方式操作。
# 矩阵乘积可以使用点函数或方法来执行：
print("*-"*40)
a=np.array([[1,1],[0,1]])
b=np.array([[2,0],[3,4]])
print("a=",a)
print("b=",b)
print("a*b=",a*b)
print("a.dot(b)=",a.dot(b))
print("np.dot(a,b)=",np.dot(a,b))
a+=b
print("a=",a)
a*=3
print("a=",a)
print("*-"*40)
print("a.sum()=",a.sum())
print("a.min()=",a.min())
print("a.max()=",a.max())
#默认情况下，这些操作适用于数组，就像它是一个数字列表，
#而不管其形状。 但是，通过指定轴参数，可以沿着数组的指
#定轴应用操作：
print("*-"*40)
b = np.arange(12).reshape(3,4)
print("b=",b)
print("b.sum(axis=0)=",b.sum(axis=0))
print("b.min(axis=0)=",b.min(axis=0))
print("b.cumsum(axis=0)=",b.cumsum(axis=0)) #每行的累积和
#NumPy提供了熟悉的数学函数，如sin，cos和exp。 在NumPy中，这
#些被称为“通用函数”（ufunc）。 在NumPy中，这些函数在数组上
#按元素操作，产生一个数组作为输出
b = np.arange(3)
print("b=",b)
print("np.exp(b)=",np.exp(b))
print("np.sqrt(b)=",np.sqrt(b))
c = np.array([2., -1., 4.])
print("c=",c)
print("np.add(b,c)=",np.add(b,c))
#Indexing, Slicing and Iterating索引，切片和迭代
#一维数组可以索引，切片和迭代，就像列表和其他Python序列一样。
print("*-"*40)
a=np.arange(10)**3
print("a=",a)
print("a[2]=",a[2])
print("a[2:5]=",a[2:5])
print("a[:6:2]=",a[:6:2]) #等效于a[0:6:2]
print("a[::-1]=",a[::-1])
for i in a:
	print("i**(1/3.)=",i**(1/3.))
#多维数组可以每个轴有一个索引。 这些索引以逗
#号分隔的元组给出：
