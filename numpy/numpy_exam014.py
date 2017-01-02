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
#多维数组可以每个轴有一个索引。 这些索引以逗
#号分隔的元组给出：
def f(x,y):
	return 10*x+y
b = np.fromfunction(f,(5,4),dtype=int)
print("b=",b)
print("b[2,3]=",b[2,3])
print("b[0:5,1]=",b[0:5,1])
print("b[:,1]=",b[:,1])
print("b[1:3,:]=",b[1:3,:])