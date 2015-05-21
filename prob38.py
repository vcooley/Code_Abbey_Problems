__author__ = 'Vince'

from math import sqrt

# -B +- sqrt(B ^ 2 - 4AC) / 2A
inp = open('test.txt')
out = open('result.txt', 'r+')
N = int(inp.readline())

def find_root(a, b , c):
    # first check if complex number
    rtarg = b ** 2.0 - 4.0 * a * c
    if rtarg < 0.0:
        # Complex root
        rtarg *= -1.0
        coi = int(sqrt(rtarg) / (2.0 * a))
        ba = int((-1.0 * b) / (2.0 * a))
        return "%d+%di %d-%di; " % (ba, coi, ba, coi)

    else:
        # Real root.
        root1 = (-1 * b + sqrt(rtarg)) / (2 * a)
        root2 = (-1 * b - sqrt(rtarg)) / (2 * a)
        return "%d %d; " % (root1, root2)




for i in range(N):
    abc = map(float, inp.readline().split())
    print abc
    a = abc[0]
    b = abc[1]
    c = abc[2]
    out.write(find_root(a, b, c))
