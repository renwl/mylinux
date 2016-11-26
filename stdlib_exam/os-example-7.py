import os

os.mkdir("test")
os.rmdir("test")

os.rmdir("samples") # this will fail
#os.removedirs("samples/sss") # this will fail
## Traceback (innermost last):
##   File "os-example-7", line 6, in ?
## OSError: [Errno 41] Directory not empty: 'samples'
