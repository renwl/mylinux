import sys

def dump(module):
    print(module, "=>",end=" ")
    if module in sys.builtin_module_names:
        print("<BUILTIN>")
    else:
        module = __import__(module)
        print(module.__file__)

dump("os")
dump("sys")
dump("string")
dump("zlib")
dump("strop")

## os => C:\python\lib\os.pyc
## sys => <BUILTIN>
## string => C:\python\lib\string.pyc
## strop => <BUILTIN>
## zlib => C:\python\zlib.pyd
