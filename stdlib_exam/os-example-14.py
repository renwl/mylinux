import os       
import time       
       
pid = os.fork() 
print("pid=",pid)      
if pid:       
    os._exit(0) # kill original  
       
print("daemon started")       
time.sleep(10)       
print("daemon terminated")       
