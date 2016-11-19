#coding=utf-8
import urllib.request, urllib.error, urllib.parse   
doc = urllib.request.urlopen("http://www.baidu.com").read()    
print("doc=",doc.decode("gbk","ignore"))
doc = urllib.request.urlopen("http://www.baidu.com")    
print("doc info=",doc.info())
print("header file=",dir(doc.info()))
url = r"http://fun.youth.cn/zutulist/201611/W020161116538078545609.jpg"   
path = r"e:\1.jpg"   
data = urllib.request.urlopen(url).read()     
f = open(path,"wb")     
f.write(data)     
f.close()