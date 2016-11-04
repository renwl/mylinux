#! /usr/bin/env python
import sys
sys.path.append("./mypy")
import os
import re
from NetChange import *
from FileSize import *

if len(sys.argv) < 2:
	print "please input simulation filename!"
else:
	SimPath=re.split(r'/',sys.argv[1])
	SimFile=re.split('\.',SimPath[-1])
	#f_sim=open(sys.argv[1])
	#for FileLine in f_sim:
	#	if re.search(r"design\(",FileLine):
	#		NetPath=re.split('\"',FileLine)[1]
	#		print NetPath

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
	exitFlag=0
	for eachline in f_sim:
		if re.search(r"exit\(",eachline):
			exitFlag=1	
	f_sim.close()
	if exitFlag==0:
		f_sim=open(sys.argv[1],"a")
		f_sim.write("\n")
		f_sim.write(r"exit()")
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
			if re.search("^desVar",eachline):
				LData.append(eachline)
				for parkey in patternline:
					if re.search(parkey,eachline):
						tt=r"desVar(	  " + ' \"' +parkey + '\"' + " " + patternline[parkey] + "	)\n"
						LData.pop()
						LData.append(tt)
			elif re.search(r"\'temp",eachline):
				tt="		\'temp" + ' \"' + patternline["temp"] + '\"' + '\n'
				LData.append(tt)
			elif re.search(r"^temp",eachline):
				tt=r"temp( " + patternline["temp"] + " )\n"
				LData.append(tt)
			else:
				LData.append(eachline)
		f_sim.close()
		f1=open(sys.argv[1],"w")
		for i in LData:
			f1.write(i)
		f1.close()
		if os.path.exists(SimFile[0] + r'.log'):
			os.remove(SimFile[0] + r'.log')
		print "start simulation"
		LocalPath=r'ocean -nograph < ' + SimPath[-1] + r" > " + SimFile[0] + r'.log'
		os.system(LocalPath)
		print "run simulation result output"
		f=open(SimFile[0] + r".csv","a")
		f1=open(SimFile[0] + r'.log')
		MeasData=[]
		ResFlag=0
		temp3=[]
		for parkey in patternline:
			temp3.append(parkey + "=" + str(patternline[parkey]))
		ResultLine=",".join(temp3) 
		MeasData.append(ResultLine + "\n")
		for i in f1:
			if re.search(r"Summary statistics:",i):
				ResFlag=1
				MeasData.append(i)
				continue
			elif ResFlag==1:
				if re.search("Total",i):
					ResFlag=0
				else:
					MeasData.append(i)
		for i in MeasData:
			if re.search(r"^$\s*",i):
				pass
			else:
				f.write(i)
		f.close()
		f1.close()
		print "finish simulation"
	
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
