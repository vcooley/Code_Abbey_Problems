"""
Matching Words
Code Abbey Problem 55
"""

__author__ = 'Vince'

def match_finder(word_list):
    """
    Takes a list of words and finds the words that are duplicated in that list.
    :param word_list:
    :return match_list:
    """
    dupe_check = []
    match_list = []
    for word in word_list:
        if word in match_list:
            continue
        elif word in dupe_check:
            match_list.append(word)
        else:
            dupe_check.append(word)
    return match_list


with open('test.txt') as data_file:
    words = data_file.read().split()
    matches = sorted(match_finder(words))
    for match in matches:
        print match,
