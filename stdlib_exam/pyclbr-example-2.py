import pyclbr
import string

mod = pyclbr.readmodule("cgi")

def dump(c):
    # print class header
    s = "class " + c.name
    if c.super:
        s = s +  "(" + string.join([v.name for v in c.super], ", ") + ")"
    print(s + ":")
    # print method names, sorted by line number
    methods = list(c.methods.items())
    methods.sort(lambda a, b: cmp(a[1], b[1]))
    for method, lineno in methods:
        print("  def " + method)
    print()

for k, v in list(mod.items()):
    dump(v)

## class MiniFieldStorage:
##   def __init__
##   def __repr__
##
## class InterpFormContentDict(SvFormContentDict):
##   def __getitem__
##   def values
##   def items
##
## ...
