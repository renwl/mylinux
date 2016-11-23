exec(compile(open("hello.py").read(), "hello.py", 'exec'))

def EXECFILE(filename, locals=None, globals=None):
    exec(compile(open(filename).read(), filename, "exec"), locals, globals)

EXECFILE("hello.py")

## hello again, and welcome to the show
## hello again, and welcome to the show
