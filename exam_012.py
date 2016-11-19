#coding=utf-8   
#http://www.tuicool.com/articles/V36vyuJ
#Python3学习笔记（urllib模块的使用）
from urllib import request                                                                                                  
response = request.urlopen(r'http://python.org/') # <http.client.HTTPResponse object at 0x00000000048BC908> HTTPResponse类型
page = response.read()                                                                                                      
page = page.decode('utf-8')    
print(page)                                                                                             