import os
import re

def run(program, *args, **kw):
    # find executable
    print("args=",args)
    print("kw=",kw)
    mode = kw.get("mode", os.P_WAIT)
    #for path in string.split(os.environ["PATH"], os.pathsep):
    for path in re.split(os.pathsep,os.environ["PATH"]):
        file = os.path.join(path, program) + ".exe"
        try:
            return os.spawnv(mode, file, (file,) + args)
        except os.error:
            pass
    raise os.error("cannot find executable")

#run("python", "hello.py", mode=os.P_NOWAIT)
run("python", "hello.py", mode=os.P_WAIT)
print("os.p_nowait=",os.P_NOWAIT)
print("os.p_wait=",os.P_WAIT)
print("goodbye")

## goodbye
## hello again, and welcome to the show
