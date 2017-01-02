#! /usr/bin/env python
import time
StartTime=time.time()
import sys
sys.path.append("./mypy")
import os
import re
from NetChange import *
from FileSize import *
Tcount=0
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
		SingleRunStart=time.time()
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

		#LocalPath=r'spectremdl ++aps +mt=4 -format psfbin -batch ' + SimFile[0] + '_runc.mdl -tab -design ./' + SimPath[-1]
		LocalPath=r'spectremdl +mt=1 -format psfbin -batch ' + SimFile[0] + '_runc.mdl -tab -design ./' + SimPath[-1]
		LocalPath=LocalPath + r" -measure " + SimFile[0] + r'.measure'
		os.system(LocalPath)

		f=open(SimFile[0] + r".csv","a")
		f1=open(SimFile[0] + r'.measure')
		MeasData=[]
		for i in f1:
			temp=re.sub(r"\s+"," ",i)
			temp1=re.sub(r"^\s+","",temp)
			temp2=re.sub(r"\s",",",temp1)
			if re.search("^\s*$",temp2):
				pass
			elif re.search("^[a-zA-Z]",temp2) and not(re.search(r"^NaN",temp2)):
				if SimChoice==1 and int(patternline["index"])==0:
					temp3=[]
					for parkey in patternline:
						temp3.append(parkey)
					ResultLine=",".join(temp3) + "," + temp2
					if len(MeasData):
						MeasData.pop(0)
					MeasData.append(ResultLine + "\n")
				else:
					pass
			else:
				temp3=[]
				for parkey in patternline:
					temp3.append(str(patternline[parkey]))
				ResultLine=",".join(temp3) + "," + temp2
				MeasData.append(ResultLine + "\n")
		for i in MeasData:
			f.write(i)
			#f.write(patternline + "," + i)
		f.close()
		f1.close()
	
		StartIndex+=1
		f=open(SimFile[0] + r"_IndexList.txt","w")
		f.write("index=" + str(StartIndex))
		f.close()
		if Tcount==0:
			TranPath=r"./" + SimFile[0] + r'.raw'
			print "simulation result path=",TranPath
			TranSize=filesize(TranPath)
			print "simulation result size=",TranSize
			Tcount=1
		now=time.time()
		print "total time=",now - StartTime
		print "single run time=",now - SingleRunStart
		if TranSize <= 5e5:
			pass
		elif ((5e5 < TranSize <= 1e6) and ((now - StartTime) > (Tcount * 3600))):
			Tcount+=1
			f_size=filesize(".")
			if f_size > 50e6:
				print "overflow",f_size
				input("continue?")
			else:
				print "safe",f_size
		elif TranSize > 1e6:
			f_size=filesize(".")
			if f_size > 50e6:
				print "overflow",f_size
				input("continue?")
			else:
				print "safe",f_size	
		else:
			pass
