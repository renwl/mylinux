import msvcrt

print("press 'escape' to quit...")

while 1:
    char = msvcrt.getch()
    if char == chr(27):
        break
    print(char, end=' ')
    if char == chr(13):
        print()

## press 'escape' to quit...
## h e l l o
