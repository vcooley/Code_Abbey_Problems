__author__ = 'Vince'

"""Multisided dice. Given a set of numbers (last number in set indicated by 0)
find choose the likeliest die set for those numbers. Dice can have 2, 4, 6, 8,
10, or 12 sides. All dice in a set will have the same number of sides."""

# Average value of a n-sided die roll is (n+1) / 2.
# Average value of m n-sided dice rolls must be m * ((n+1) / 2).
# So given an average value of an unknown number of unknown sided dice,
# We should find a number, m which when divided by that average, gives us n

from numpy import mean

def number_of_dice(rolls, max_dice=5, sides='even'):
    """Finds how many dice were rolled given a rollset.
    All dice must be the same sidedness. Odd-sided dice not yet implemented.
    Method is not 100% accurate due to the probabalistic nature of the problem
    """
    # If 1 is in the rollset then there must be exactly one die.
    if 1 in rolls:
        return 1
    # Otherwise we don't know the number of dice, let's make an educated guess
    # using the fact that there are not more than 5 dice in this problem.

    # Represents the most accurate number of dice so far
    closest = 1
    # Represents the difference between a float and its int. Get close to 0.5
    d_value = 1

    for i in range(1, max_dice + 1):
        # Divide the mean of the rolls by 1 - max_dice, and store results
        # only if the truncated value is odd.
        r = float(mean(rolls)) / i
        if int(r) % 2 != 0:
            r -= int(r)
            r = abs(r)
            if r < d_value:
                d_value = r
                closest = i
    return closest


def side_finder(rolls, dice_number):
    """Finds how many sides a set of dice have given a rollset and a number
    of dice. Odd sided dice not yet implemented. All dice must have the
    same sidedness.
    """
    average = mean(rolls)
    roll_average = average / dice_number
    # This is the part that doesn't work for odd sided dice
    die_sides = round(roll_average * 2 + 1)
    return die_sides


if __name__ == "__main__":
    inp = open('test.txt')
    for i in range(3):
        rollSet = map(int, inp.readline().split())
        del rollSet[len(rollSet) - 1]
        number = number_of_dice(rollSet)
        sides = side_finder(rollSet, number)
        print "%dd%d" % (number, sides)