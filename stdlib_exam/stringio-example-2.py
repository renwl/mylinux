import io

file = io.StringIO()
file.write("This man is no ordinary man. ")
file.write("This is Mr. F. G. Superman.")

print(file.getvalue())

## This man is no ordinary man. This is Mr. F. G. Superman.
