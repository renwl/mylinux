import traceback
import io

try:
    raise IOError("an i/o error occurred")
except:
    fp = io.StringIO()
    traceback.print_exc(file=fp)
    message = fp.getvalue()

    print("failure! the error was:", repr(message))

## failure! the error was: 'Traceback (innermost last):\012  File
## "traceback-example-2.py", line 5, in ?\012IOError: an i/o error
## occurred\012'
