def open(filename, mode="rb"):
    import builtins
    file = builtins.open(filename, mode)  
    #PicCont= file.read(5).decode("utf-8")
    PicCont= file.read(5)
    print("file=",PicCont)
    if PicCont not in(b"GIF87", b"GIF89"):
        raise IOError("not a GIF file")
    file.seek(0)
    return file

fp = open(r"e:\dd.gif")
print(len(fp.read()), "bytes")

fp = open(r"e:\1.jpg")
print(len(fp.read()), "bytes")

## 3565 bytes
## Traceback (innermost last):
##   File "builtin-open-example-1.py", line 12, in ?
##   File "builtin-open-example-1.py", line 5, in open
## IOError: not a GIF file
