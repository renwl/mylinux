#coding=utf-8
"""
Python图表绘制：matplotlib绘图库入门
matplotlib 是python最著名的绘图库，它提供了一整套和matlab相似的命令API，
十分适合交互式地行制图。而且也可以方便地将它作为绘图控件，嵌入GUI应用程序中。
它的文档相当完备，并且Gallery页面中有上百幅缩略图，打开之后都有源程序。因此
如果你需要绘制某种类型的图，只需要在这个页面中浏览/复制/粘贴一下，基本上都能搞定。
在Linux下比较著名的数据图工具还有gnuplot，这个是免费的，Python有一个包可以调用gnuplot，
但是语法比较不习惯，而且画图质量不高。
而 Matplotlib则比较强：Matlab的语法、python语言、latex的画图质量
（还可以使用内嵌的latex引擎绘制的数学公式）。 
本文目录
1. Matplotlib.pyplot快速绘图
2. 面向对象画图
3. Matplotlib.pylab快速绘图
4. 在图表中显示中文
5. 对LaTeX数学公式的支持
6. 对数坐标轴
7. 学习资源
 
Matplotlib.pyplot快速绘图
快速绘图和面向对象方式绘图
matplotlib实际上是一套面向对象的绘图库，它所绘制的图表中的每个绘图元素，
例如线条Line2D、文字Text、刻度等在内存中都有一个对象与之对应。
为了方便快速绘图matplotlib通过pyplot模块提供了一套和MATLAB类似的绘图API，
将众多绘图对象所构成的复杂结构隐藏在这套API内部。我们只需要调用pyplot模块
所提供的函数就可以实现快速绘图以及设置图表的各种细节。pyplot模块虽然用法简单，
但不适合在较大的应用程序中使用。
为了将面向对象的绘图库包装成只使用函数的调用接口，pyplot模块的内部保存了当前
图表以及当前子图等信息。当前的图表和子图可以使用plt.gcf()和plt.gca()获得，分别
表示"Get Current Figure"和"Get Current Axes"。在pyplot模块中，许多函数都是对当
前的Figure或Axes对象进行处理，比如说：
    plt.plot()实际上会通过plt.gca()获得当前的Axes对象ax，然后再调
    用ax.plot()方法实现真正的绘图。
可以在Ipython中输入类似"plt.plot??"的命令查看pyplot模块的函数是
如何对各种绘图对象进行包装的。
配置属性
matplotlib所绘制的图表的每个组成部分都和一个对象对应，我们可以通过
调用这些对象的属性设置方法set_*()或者pyplot模块的属性设置函数setp()设置它们的属性值。
因为matplotlib实际上是一套面向对象的绘图库，因此也可以直接获取对象的属性
配置文件
绘制一幅图需要对许多对象的属性进行配置，例如颜色、字体、线型等等。
我们在绘图时，并没有逐一对这些属性进行配置，许多都直接采用了matplotlib的缺省配置。
matplotlib将这些缺省配置保存在一个名为“matplotlibrc”的配置文件中，通过修改配置文件，
我们可以修改图表的缺省样式。配置文件的读入可以使用rc_params()，它返回一个配置字典；
在matplotlib模块载入时会调用rc_params()，并把得到的配置字典保存到rcParams变量中；
matplotlib将使用rcParams字典中的配置进行绘图；用户可以直接修改此字典中的配置，
所做的改变会反映到此后创建的绘图元素。
绘制多子图（快速绘图）
Matplotlib 里的常用类的包含关系为 Figure -> Axes -> (Line2D, Text, etc.)
一个Figure对象可以包含多个子图(Axes)，在matplotlib中用Axes对象表示一个绘图区域，
可以理解为子图。
可以使用subplot()快速绘制包含多个子图的图表，它的调用形式如下：
subplot(numRows, numCols, plotNum)
subplot将整个绘图区域等分为numRows行* numCols列个子区域，然后按照从左到右，
从上到下的顺序对每个子区域进行编号，左上的子区域的编号为1。如果numRows，numCols和plotNum
这三个数都小于10的话，可以把它们缩写为一个整数，例如subplot(323)和subplot(3,2,3)是相同的。
subplot在plotNum指定的区域中创建一个轴对象。如果新创建的轴和之前创建的轴重叠的话，之前的
轴将被删除。
"""
import numpy as np                         
                                           
import matplotlib.pyplot as plt            
                                           
                                           
                                           
plt.figure(1) # 创建图表1                  
                                           
plt.figure(2) # 创建图表2                  
                                           
ax1 = plt.subplot(211) # 在图表2中创建子图1
                                           
ax2 = plt.subplot(212) # 在图表2中创建子图2
                                           
                                           
                                           
x = np.linspace(0, 3, 100)                 
                                           
for i in range(5):                        
                                           
	plt.figure(1)  #? # 选择图表1          
	                                       
	plt.plot(x, np.exp(i*x/3))   
	#plt.figure(2)          
	                                       
	plt.sca(ax1)   #? # 选择图表2的子图1   
	                                       
	plt.plot(x, np.sin(i*x))      
	#plt.figure(2)        
	                          
	                                     
	plt.sca(ax2)  # 选择图表2的子图2       
	                                       
	plt.plot(x, np.cos(i*x))               
                                           
                                           
                                           
plt.show()                                 