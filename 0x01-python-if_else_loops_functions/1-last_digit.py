#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
Lastdigit = abs(number) % 10
if number < 0:
    Lastdigit = -Lastdigit
print("Last digit of {} is {} and is ".format(number, Lastdigit), end="")
if Lastdigit > 5:
    print("greater than 5")
elif Lastdigit == 0:
    print("0")
else:
    print("less than 6 and not 0")
