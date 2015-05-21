__author__ = 'Vince'

import math


class Guesser(object):

    def __init__(self, a, b, c, d):
        self.a = a
        self.b = b
        self.c = c
        self.d = d

    def expression(self, x):
        result = self.a * x + self.b * math.sqrt(x ** 3) - self.c * math.exp(-x / 50) - self.d
        return result


def guess(low, high):
    guess = (high + low) / 2
    return guess

def solution(abcd):
    a = abcd[0]
    b = abcd[1]
    c = abcd[2]
    d = abcd[3]
    precision = 0.0000001
    bottom = 0.0
    top = 100.0
    x = guess(bottom, top)
    guesser = Guesser(a, b, c, d)

    not_close_enough = True
    while not_close_enough:
        x_val = guesser.expression(x)
        if abs(x_val) < precision:
            not_close_enough = False
            break
        elif x_val > 0:
            top = x
            x = guess(bottom, top)
        else:
            bottom = x
            x = guess(bottom, top)
    return x


inp = open('test.txt')
N = int(inp.readline())

for k in range(N):
    abcd = inp.readline()
    abcd = map(float, abcd.split())
    print solution(abcd),