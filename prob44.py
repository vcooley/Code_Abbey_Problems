__author__ = 'Vince'

def rand_int_to_dice(rando, die_sides=6):
    """Converts a random number to it's associated die value."""
    die_value = rando % die_sides + 1
    return  die_value

inp = open('test.txt')
N = int(inp.readline())
for dummy_i in range(N):
    dice = inp.readline().split()
    print rand_int_to_dice(int(dice[0])) + rand_int_to_dice(int(dice[1])),
inp.close()