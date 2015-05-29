__author__ = 'Vince'


def convert_to_dice(prob, n):
    """Takes probability and converts it to the appropriate
    number on an n-sided die.
    """
    die_roll = int(prob * n) + 1
    return die_roll

inp = open('test.txt')
N = int(inp.readline())
for i in range(N):
    probability = float(inp.readline())
    print convert_to_dice(probability, 6),
inp.close()