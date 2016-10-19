#! /usr/bin/env python
import sys
sys.path.append("./mypy")
import os
import re
from NetChange import *
ListStart=1e-3
ListStep=1e-3
ListStop=100e-3
temp_parlist=[-40,27,85]
cor_parlist=["snfp","fnsp","ss","tt","ff"]
vdd_parlist=[1.35,1.55]

if len(sys.argv) < 2:
	print "please input simulation filename!"
else:
	temp1=re.split(r'/',sys.argv[1])
	temp=re.split('\.',temp1[-1])
	x=ListStart
	gain_parlist=[x];
	while 1:
		x+=ListStep
		if x >  ListStop:
			break
		gain_parlist.append(x)
	SimChoice=int(input("please input 1 for new simulation,0 for continue"))
	if SimChoice==1 :
		f=open(temp[0] + "_CorList.txt","w")
		for gain_par in gain_parlist:
			for vdd_par in vdd_parlist:
				for temp_par in temp_parlist:
					for cor_par in cor_parlist:
						f.write(str(gain_par) + " " + str(vdd_par) + " " + str(temp_par) + " " + str(cor_par) + "\n")
		f.close()


	if SimChoice==1 :
		f=open(temp[0] + r".csv","w")
		f.write("start simulation\n")
		f.close()
	f_sim=open(sys.argv[1])
	LData=[]
	tt=""
	for eachline in f_sim:
		if re.search("mylib",eachline):
			if re.search("mylib_smic95",eachline):
				tt=LibCh("smic95")
				LData+=tt
			else:
				tt=LibCh("smicee")
				LData+=tt
		else:
			LData.append(eachline)
	f_sim.close()
	f_sim=open(sys.argv[1],"w")
	for i in LData:
		f_sim.write(i)
	f_sim.close()

	f=open(temp[0] + "_CorList.txt","r")
	PatternData=f.readlines()
	StoreData=PatternData[:]
	f.close()
	
	for patternline in PatternData:
		f_sim=open(sys.argv[1])
		l=patternline.split(" ")
		LData=[]
		tt=""
		for eachline in f_sim:
			if re.search("gain=",eachline):
				tt=ParCh("gain",l[0],eachline)
				tt=ParCh("vdd",l[1],tt)
				LData.append(tt)
			elif re.search("temp=",eachline):
				tt=ParCh("temp",l[2],eachline)
				LData.append(tt)
			elif re.search("section=",eachline):
				tt=CorCh(l[3],eachline)
				LData+=tt
			else:
				LData.append(eachline)
		f_sim.close()
		f1=open(sys.argv[1],"w")
		for i in LData:
			f1.write(i)
		f1.close()
		LocalPath=r'spectremdl ++aps +mt=4 -format psfbin -batch ' + temp[0] + '_runc.mdl -tab -design ./' + temp1[-1]
		LocalPath=LocalPath + r" -measure " + temp[0] + r'.measure'
		os.system(LocalPath)
		
		f=open(temp[0] + r".csv","a")
		f.write("gain=" + l[0] + " vdd=" + l[1] + " temp=" + l[2] + " corner=" + l[3])
		f1=open(temp[0] + r'.measure')
		TempData=[]
		for i in f1:
			if re.search("^\s*$",i) or re.search(r":",i):
				pass
			else:
				TempData.append(i)
		for i in TempData:
			f.write(i)
		f.close()
		f1.close()
	
		StoreData.pop(0)
		f=open(temp[0] + "_CorList.txt","w")
		for i in StoreData:
			f.write(i)
		f.close()

