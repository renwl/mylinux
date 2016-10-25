#! /usr/bin/env python
import sys
sys.path.append("./mypy")
import os
import re
from NetChange import *
SimCond={}
SimCond["temp"]=[-40,27,85]
SimCond["cor"]=["snfp","ss","tt","ff"]
SimCond["vdd"]=[1.4,1.5]
SimCond["gain"]=[i*1e-3 for i in range(1,11,1)]
SimCond["rl"]=[2.1e3,3.1e3]



if len(sys.argv) < 2:
	print "please input simulation filename!"
else:
	filename=sys.argv[1].split(r".")[0]
	#print "filename=",filename
	#SimChoice=int(input("please input 1 for new simulation,0 for continue"))
	SimChoice=1
	if SimChoice==1 :
		index=0
		f=open(filename + r"_CorList.txt","w")
		keylist=[]
		lenpar=1
		for keys in SimCond:
			keylist.append(keys)
			lenpar*=len(SimCond[keys])
		#print keylist
		#print "length=",lenpar
		ParTemp={}
		for paridx in range(0,lenpar,1):
			strtemp="index," + str(paridx)
			ParTemp[paridx]=[strtemp]
		for keys in SimCond:
			lentemp=len(SimCond[keys])
			for i in ParTemp:
				strtemp=keys + "," + str(SimCond[keys][i%lentemp])
				ParTemp[i].append(strtemp)	
		for keys in ParTemp:
			strtemp=",".join(ParTemp[keys]) + ";\n"
			#print keys,"------",strtemp
			f.write(strtemp)
		f.close()
"""
			for par in vdd_parlist:
				for temp_par in temp_parlist:
					for cor_par in cor_parlist:
						f.write("index," + str(index) + "," + "gain," + str(gain_par) + "," + "vdd," + str(vdd_par) + "," + 
						"temp," + str(temp_par) + "," + "cor," + str(cor_par) + ";\n")
						index+=1
		f.close()
"""
