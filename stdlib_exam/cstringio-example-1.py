import io

MESSAGE = "That man is depriving a village somewhere of a computer scientist."

file = io.StringIO(MESSAGE)

print(file.read())

## That man is depriving a village somewhere of a computer scientist.
