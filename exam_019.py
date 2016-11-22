#! /usr/bin/env python                                                   
#coding=utf-8                                                            
                                                                         
import glob, os                                                          
modules = []                                                             
for module_file in glob.glob("*-plugin.py"):                             
	try:    
		print("module_file=",module_file)                                                             
		module_name, ext =os.path.splitext(os.path.basename(module_file))  
		print("module_name=",module_name)
		print("ext=",ext)
		module = __import__(module_name)                                 
		modules.append(module)
		print("module=",module)  
		                                         
	except ImportError:                                                  
		pass # ignore broken modules                                     
# say hello to all modules                                               
for module in modules:                                                   
	module.hello()                                                       