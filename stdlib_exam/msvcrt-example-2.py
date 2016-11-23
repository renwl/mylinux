import msvcrt
import time

print("press SPACE to enter the serial number")

while not msvcrt.kbhit() or msvcrt.getch() != " ":
    # do something else
    print(".", end=' ')
    time.sleep(0.1)

print()

# clear the keyboard buffer
while msvcrt.kbhit():
    msvcrt.getch()

serial = input("enter your serial number: ")

print("serial number is", serial)

## press SPACE to enter the serial number
## . . . . . . . . . . . . . . . . . . . . . . . .
## enter your serial number: 10
## serial number is 10
