#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
lastDigit = int(repr(number)[-1])
standard = "Last digit of {} is {} and is".format(number, lastDigit)
if lastDigit > 5:
    print("{}greater than 5\n".format(standard))
elif lastDigit == 0:
    print("{}0\n".format(standard))
else:
    print("{}less than 6 and not 0\n".format(standard))
