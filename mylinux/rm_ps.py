#! /usr/bin/env python
import sys
import os
import re
tmp=os.popen(r'ps -t').readlines()
for i in tmp:
	if re.search(r"rm_ps",i):
		pass
	else:
		if re.search("perl",i) or re.search("python",i) or re.search("spectre",i) or re.search(r"awd.exe",i):
			#print i
			aaa=re.split("\s*[p]",i)[0]
			bbb=aaa.split(" ")[-1]
			#print "pid=",bbb
			os.system('kill -9 ' + str(bbb))
