"""
Blackjack Counting
Find the best possible score of a hand. Return 'Bust' if
no scoring results in a hand of less than 21.
"""

__author__ = 'Vince'

def blackjack_scorer(hand):
    """
    Takes a hand as an array and returns a blackjack score.
    :param hand:
    :return score:
    """
    aces = 0
    score = 0
    for card in hand:
        try:
            score += int(card)
        except ValueError:
            if card == 'A':
                aces += 1
            else:
                score += 10
    best = score + aces
    test = best
    if aces != 0:
        test = score + 11 + aces - 1
    if best < test <= 21:
        return test
    elif best > 21:
        return "Bust"
    else:
        return best

with open('test.txt') as data_file:
    N = int(data_file.readline())
    for i in range(N):
        print blackjack_scorer(data_file.readline().split()),
