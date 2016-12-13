#! /usr/bin/env python
import sys
import os
import re
import glob

#SearchPattern=re.compile(r"always\s*@\(\*")
SearchPattern=re.compile(r"SPICE Explorer")
if len(sys.argv) < 2:
	print('no argument! please input filename and pattern!')
else:
	if re.search(r"\*",sys.argv[1]):
		pass
	else:
		print "no meta char , if this is not what you want , add ''"
		input("continue?")
	for file in glob.glob(sys.argv[1]):
		#print file
		try:
			f=open(file,'r')
			count=1
			index=0
			for eachline in f:
					if SearchPattern.search(eachline):
						if index==0:
							print file
						print count,"	",eachline
						index=1
					count+=1
			f.close()
		except IOError, e:
			print "*** file open error :", e