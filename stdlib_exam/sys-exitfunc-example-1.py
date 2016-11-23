import sys
import atexit

def exitfunc():
    print("world")

atexit.register(exitfunc)

print("hello")
sys.exit(1)
print("there") # never printed

## hello
## world
