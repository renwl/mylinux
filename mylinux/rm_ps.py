#! /usr/bin/env python
import sys
import os
import re
tmp=os.popen(r'ps').readlines()
for i in tmp:
	if re.search("perl",i) or re.search("python",i) or re.search("spectre",i):
		aaa=re.split("\s*[p]",i)[0]
		bbb=aaa.split(" ")[-1]
		os.system('kill -9 ' + str(bbb))