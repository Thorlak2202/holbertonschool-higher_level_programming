#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    last = (number*(-1)) % 10
else:
    last = number % 10
if last > 5:
    print("Last digit of {:d} is {:d} and is \
greater than 5" .format(number, last))
if last == 0:
    print("Last digit of {:d} is {:d} and is zero" .format(number, last))
if last < 6 and last != 0:
    print("Last digit of {:d} is {:d} and is \
less than 6 and not 0" .format(number, last))
