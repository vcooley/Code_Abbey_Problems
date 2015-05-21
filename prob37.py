from math import ceil
from decimal import *
# 3400000 3 78
p = 3400000.0
r = 1.0 + 0.03/12.0
time = 78
guess = p / time
total = p
print p, r, time, guess, total
while total > 0:
    total = p
    for i in range(time):
        total *= r
        total -= guess
    guess += 1
print guess
