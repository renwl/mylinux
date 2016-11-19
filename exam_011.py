#!/usr/bin/python 
#coding=utf-8 
import urllib.request, urllib.parse, urllib.error 
import urllib.request, urllib.error, urllib.parse 
def post(url, data): 
	req = urllib.request.Request(url) 
	data = urllib.parse.urlencode(data) 
	#enable cookie 
	opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor()) 
	response = opener.open(req, data) 
	return response.read() 
def main(): 
	posturl = "http://" 
	data = {'email':'mpassport.baidu.compassport.baidu.compassport.baidu.comass', 'autologin':'1', 'submit':'登 录', 'type':''} 
	print(post(posturl, data)) 
if __name__ == '__main__': 
	main() 