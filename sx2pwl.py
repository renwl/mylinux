#! /usr/bin/env python
import sys
import os
import re
SearchPattern=re.compile(r"^\+\s* | ^\+\)")
NoDigit=re.compile("^[^\d]")
if len(sys.argv) < 2:
	print('no argument! please input filename!')
else:
	try:
		f=open(sys.argv[1],'r')
		da=[]
		for eachline in f:
			replaceline=SearchPattern.sub("",eachline)
			if NoDigit.search(replaceline):
				pass
			else:
				replaceline1=SearchPattern.sub("",replaceline)
				da.append(replaceline1)	
		f.close()
	except IOError, e:
		print "*** file open error :", e
	try:
		f=open(sys.argv[1],'w')
		for eachline in da:
			#print eachline
			f.writelines(re.sub('\,',' ',eachline))
		f.close()
	except IOError, e:
		print "*** file open error :", e