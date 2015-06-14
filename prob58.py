"""
Card Names
Find the suit and rank of a card given its number in the deck.
"""

__author__ = 'Vince'


def find_card_name(card_val):
    """
    Given the card number in a 52 card deck, returns the ranks
    and suit of a card.
    :param card_val:
    :return card_suit:
    :return card_rank:
    """
    suits = ['Clubs', 'Spades', 'Diamonds', 'Hearts']
    ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10',
             'Jack', 'Queen', 'King', 'Ace']
    card_suit = suits[card_val / 13]
    card_rank = ranks[card_val % 13]
    return card_suit, card_rank


with open('test.txt') as data_file:
    N = int(data_file.readline())
    card_list = map(int, data_file.readline().split())
    for card in card_list:
        suit, rank = find_card_name(card)
        print "%s-of-%s" % (rank, suit),
