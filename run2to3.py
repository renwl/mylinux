#! /usr/bin/env python
#coding=utf-8
import sys
import os
import re

tmp=os.popen(r'ls ' + sys.argv[1]).readlines()
for i in tmp:
	#print(i)
	Fpath=r'python C:\Python33\Tools\Scripts\2to3.py -w ' + i
	#print(Fpath)
	os.system(Fpath)