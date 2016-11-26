import os
import re

def run(program, *args):
	# find executable
	print("what is sep--->",os.pathsep)
	print("what is environment--->",os.environ["PATH"])
	for path in re.split(os.pathsep , os.environ["PATH"]):
		print("path=",path)
		file = os.path.join(path, program) + ".exe"
		print("file=",file)
		try:
			return os.spawnv(os.P_WAIT, file, (file,) + args)
		except os.error:
			pass
	raise os.error("cannot find executable")
	
run("python", "hello.py")

print("goodbye")

## hello again, and welcome to the show
## goodbye
