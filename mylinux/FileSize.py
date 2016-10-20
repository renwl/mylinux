import os
import re
def filesize(SrcPath):
	FileSize1=os.popen(r'du -s ' + SrcPath).readline()
	#print "my funct=",re.split("\s+",FileSize1)[0]
	return int(re.split("\s+",FileSize1)[0])
