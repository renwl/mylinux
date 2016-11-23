import tty
import os, sys

fileno = sys.stdin.fileno()

tty.setraw(fileno)
print(input("raw input: "))

tty.setcbreak(fileno)
print(input("cbreak input: "))

os.system("stty sane") # ...

## raw input: this is raw input
## cbreak input: this is cbreak input
