__author__ = 'Vince'
"""Card shuffling!"""

def deck_maker():
    ranks = ['A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K']
    suits = ['C', 'D', 'H', 'S']
    deck = []
    for i in suits:
        for k in ranks:
            deck.append(''.join([i,k]))
    return deck

def deck_shuffler(deck, number_list):
    """Takes a list of random numbers, takes each value modulo 52, then swaps
    the card in the new value with the current position in the deck.
    """
    for i in range(52):
        number = int(number_list[i]) % 52
        temp = deck[i]
        deck[i] = deck[number]
        deck[number] = temp
    return deck

inp = open('test.txt')
randoms = inp.readline().split()
shuffled = deck_shuffler(deck_maker(), randoms)
print " ".join(shuffled)
