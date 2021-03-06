#! /usr/bin/env python
import sys
sys.path.append("./mypy")
import os
import re
import shutil
from NetChange import *
from FileSize import *

if len(sys.argv) < 2:
	print "please input simulation filename!"
else:
	SimPath=re.split(r'/',sys.argv[1])
	SimFile=re.split('\.',SimPath[-1])
	SimChoice=int(input("please input 1 for new simulation,0 for continue"))
	if SimChoice==1 :
		StartIndex = 0
	else:
		f=open(SimFile[0] + r"_IndexList.txt")
		f_data=f.readline()
		StartIndex = int(f_data.split("=")[-1])
		f.close()
	print "StartIndex=",StartIndex
	if SimChoice==1 :
		f=open(SimFile[0] + r".csv","w")
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

	f_sim=open(sys.argv[1])
	LData=[]
	tt=""
	EscFlag=0
	for eachline in f_sim:
		if re.search("^parameters",eachline) and EscFlag==0:
			if re.search(r"\\$",eachline):
				EscFlag=1
				tt=re.sub(r"\\$"," ",eachline)
				tt=re.sub(r"\n","",tt)
				continue
			else:
				LData.append(eachline)
		elif EscFlag==1:
			if re.search(r"\\$",eachline):
				input("please change the source file by hand!")
			else:
				EscFlag=0
				LData.append(tt + eachline)
		else:
			LData.append(eachline)
	f_sim.close()
	f_sim=open(sys.argv[1],"w")
	for i in LData:
		f_sim.write(i)
	f_sim.close()
	PatternData=[]
	f=open(SimFile[0] + r"_CorList.txt","r")
	for i in f:
		temp1=i.split(";")[0]
		temp2=temp1.split(",")
		#print temp2
		TempData={}
		for k in range(0,len(temp2)-1,2):
			TempData[temp2[k]]=temp2[k+1]
			#print TempData
		PatternData.append(TempData)
		#PatternData=f.readlines()
	f.close()
	for patternline in PatternData:
		if int(patternline["index"]) < StartIndex:
			continue
		#print "index=",patternline["index"]
		f_sim=open(sys.argv[1])
		LData=[]
		tt=""
		for eachline in f_sim:
			if re.search("^parameters",eachline):
				for parkey in patternline:
					if parkey == "index" or parkey == "temp" or parkey == "cor":
						continue
					else:
						tt=ParCh(parkey,patternline[parkey],eachline)
						eachline=tt
						#print "tt=",tt
				LData.append(tt)
			elif re.search("temp=",eachline):
				tt=ParCh("temp",patternline["temp"],eachline)
				LData.append(tt)
			elif re.search("section=",eachline):
				tt=CorCh(patternline["cor"],eachline)
				LData+=tt 
			else:
				LData.append(eachline)
		f_sim.close()
		f1=open(sys.argv[1],"w")
		for i in LData:
			f1.write(i)
		f1.close()
		LocalPath=r'spectre ++aps +mt=4 -format psfbin ./' + SimPath[-1]
		os.system(LocalPath)
		
		SrcPath=SimFile[0] + r".raw/tran.tran"
		TarPath=SimFile[0] + r".raw/tran_" + str(StartIndex) +  ".tran"
		#SrcPath1=SimFile[0] + r".raw/"
		shutil.copyfile(SrcPath,TarPath)
		StartIndex+=1
		f=open(SimFile[0] + r"_IndexList.txt","w")
		f.write("index=" + str(StartIndex))
		f.close()
		f_size=filesize(".")
		if f_size > 50e6:
			print "overflow",f_size
			input("continue?")
		else:
			print "safe",f_size
