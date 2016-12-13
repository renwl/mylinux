import code
import string

# 
SCRIPT = [
    "a = (",
    "  1,",
    "  2,",
    "  3 ",
    ")",
    "print(a)"
]

script = ""

for line in SCRIPT:
	print("line=	",line)
	script = script + line + "\n"
	print("script=	",script, end=' ')
	co = code.compile_command(script, "<stdin>", "exec")
	if co:
		# got a complete statement.  execute it!
		print("-"*40)
		print(script, end=' ')
		print("-"*40)
		exec(co)
		script = ""
	
## ----------------------------------------
## a = (
##   1,
##   2,
##   3 
## )
## ----------------------------------------
## ----------------------------------------
## print a
## ----------------------------------------
## (1, 2, 3)
