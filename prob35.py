__author__ = 'Vince'

import decimal

def howlong(bal, tot, r):
    years = 0
    bal = decimal.Decimal(bal)
    r = decimal.Decimal(r)
    rate = r/100
    #decimal.getcontext().prec = 2
    while bal < tot:
        bal *= (1 + rate)
        bal._round_down(2)
        years += 1
    return years


inp = open('test.txt')
N = int(inp.readline())

for i in range(N):
    vals = inp.readline().split()
    print howlong(str(vals[0]), int(vals[1]), vals[2]),