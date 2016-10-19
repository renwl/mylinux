#! /usr/bin/env python
import sys
sys.path.append("./mypy")
import os
import re
from NetChange import *
ListStart=1e-3
ListStep=1e-3
ListStop=1e-3
temp_parlist=[-40,27,85]
cor_parlist=["snfp","ss","tt","ff"]
vdd_parlist=[1.4,1.5]

if len(sys.argv) < 2:
	print "please input simulation filename!"
else:
	filename=sys.argv[1].split(r".")[0]
	print "filename=",filename
	x=ListStart
	gain_parlist=[x];
	while 1:
		x+=ListStep
		if x >  ListStop:
			break
		gain_parlist.append(x)
	#SimChoice=int(input("please input 1 for new simulation,0 for continue"))
	SimChoice=1
	if SimChoice==1 :
		index=0
		f=open(filename + r"_CorList.txt","w")
		for gain_par in gain_parlist:
			for vdd_par in vdd_parlist:
				for temp_par in temp_parlist:
					for cor_par in cor_parlist:
						f.write("index," + str(index) + "," + "gain," + str(gain_par) + "," + "vdd," + str(vdd_par) + "," + 
						"temp," + str(temp_par) + "," + "cor," + str(cor_par) + ";\n")
						index+=1
		f.close()
