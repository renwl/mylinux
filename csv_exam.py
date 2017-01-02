# coding: utf-8
'''
python中对csv文件的处理，可以用一般文件读取的方式来进行，
也可以用csv模块来进行。
本例子就是给出用csv模块来进行处理的解释说明。
'''
import csv
#1. 写入并生成csv文件
#代码：
#csvfile = open('csv_test.csv', 'wb')
csvfile = open('csv_test.csv', 'w', newline = '')
writer = csv.writer(csvfile)
#xx=['姓名'.encode("utf-8"), '年龄'.encode("utf-8"), '电话'.encode("utf-8")]
#yy='姓名'.encode("utf-8")
#print(("xx=",xx))
writer.writerow(['姓名', '年龄', '电话'])
data = [
    ('小河', '25', '1234567'),
    ('小芳', '18', '789456')
]
writer.writerows(data)
csvfile.close()
'''
wb中的w表示写入模式，b是文件模式
写入一行用writerow
多行用writerows
2. 读取csv文件
代码：
'''
#csvfile = open('csv_test.csv', 'rb')
csvfile = open('csv_test.csv', 'r')
reader = csv.reader(csvfile)
for line in reader:
    print(line)
csvfile.close()
'''
运行结果：
root@he-desktop:~/python/example# python read_csv.py
['\xe5\xa7\x93\xe5\x90\x8d', '\xe5\xb9\xb4\xe9\xbe\x84', '\xe7\x94\xb5\xe8\xaf\x9d']
['\xe5\xb0\x8f\xe6\xb2\xb3', '25', '1234567']
['\xe5\xb0\x8f\xe8\x8a\xb3', '18', '789456']
'''

"""
用 python3写代码的时候发现， 使用下面的 wb打开文件，
writefile = open('result.csv','wb')
writer = csv.writer(writefile)
.
.
.
rvalue = self.traceprocess(item[0],item[1],item[6])
print(rvalue)
if rvalue:
    writer.writerow(value)
到这里用 writerow写入内容的时候 会报错，如下 ：
    writer.writerow(value)
TypeError: 'str' does not support the buffer interface
在stackoverflow上找到了比较经典的解释，原来 python3里面对 str和bytes类型做了严格的区分，
不像python2里面某些函数里可以混用。所以用python3来写wirterow时，打开文件不要用wb模式，
只需要使用w模式，然后带上newline=‘’。 
	
In Python 2.X, it was required to open the csvfile with 'b' 
because the csv module does its own line termination handling.
In Python 3.X, the csv module still does its own line termination 
handling, but still needs to know an encoding for Unicode strings.
 The correct way to open a csv file for writing is:
outputfile=open("out.csv",'w',encoding='utf8',newline='')
encoding can be whatever you require, but newline='' 
suppresses text mode newline handling. On Windows, 
failing to do this will write \r\r\n file line endings 
instead of the correct \r\n. This is mentioned in the 3.X csv.
reader documentation only, but csv.writer requires it as well.
改写的代码如下，就能正常写入了 
writefile = open('result.csv','w'，newline =‘’)
writer = csv.writer(writefile)
.
rvalue = self.traceprocess(item[0],item[1],item[6])
print(rvalue)
if rvalue:
    writer.writerow(value)
	
In Python 2.X, it was required to open the csvfile with 'b' 
because the csv module does its own line termination handling.
In Python 3.X, the csv module still does its own line termination 
handling, but still needs to know an encoding for Unicode strings. 
The correct way to open a csv file for writing is:
outputfile=open("out.csv",'w',encoding='utf8',newline='')
encoding can be whatever you require, but newline='' 
suppresses text mode newline handling. On Windows, 
failing to do this will write \r\r\n file line endings instead of 
the correct \r\n. This is mentioned in the 3.X csv.reader documentation only,
 but csv.writer requires it as well.
如果不带newline=‘’，你会发现也能写入结果，但是每行内容之间总是会多出一个空行
	
In Python 2.X, it was required to open the csvfile with 'b' because the csv 
module does its own line termination handling.
In Python 3.X, the csv module still does its own line termination handling, 
but still needs to know an encoding for Unicode strings. The correct way to 
open a csv file for writing is:
outputfile=open("out.csv",'w',encoding='utf8',newline='')
encoding can be whatever you require, but newline='' suppresses text
 mode newline handling. On Windows, failing to do this will write \r\r\n file 
 line endings instead of the correct \r\n. This is mentioned in the 3.X csv.reader
  documentation only, but csv.writer requires it as well.
下面是python参考手册里的解释，在windows这种使用\r\n的系统里，不用newline=‘’的话，
会自动在行尾多添加个\r，导致多出一个空行，即行尾为\r\r\n
If newline='' is not specified, newlines embedded inside quoted
 fields will not be interpreted correctly, and on platforms that 
 use \r\n linendings on write an extra \r will be added. It should always 
 be safe to specify newline='', since the csv module does its own (universal) newline handling.

In Python 2.X, it was required to open the csvfile with 'b' because the csv module does its 
own line termination handling.
In Python 3.X, the csv module still does its own line termination handling, but still
 needs to know an encoding for Unicode strings. The correct way to open a csv file for writing is:
outputfile=open("out.csv",'w',encoding='utf8',newline='')
encoding can be whatever you require, but newline='' suppresses text mode newline 
handling. On Windows, failing to do this will write \r\r\n file line endings instead 
of the correct \r\n. This is mentioned in the 3.X csv.reader documentation only, 
but csv.writer requires it as well.
"""
