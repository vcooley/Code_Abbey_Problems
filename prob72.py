"""
Funny Words Generator
Generate randome words where letters at odd positions are consonants and
letters at even positions are vowels. Exclude 'q' and 'y'
"""

__author__ = 'Vince'

import prob25


def funny_word_generator(random_nums):
    """
    Converts a list of random numbers into a 'funny word'
    :param random_nums:
    :return funny_word:
    """
    vowels = 'aeiou'
    consonants = 'bcdfghjklmnprstvwxz'
    funny_word = ''
    for idx, number in enumerate(random_nums):
        if idx % 2 != 0:
            funny_word += vowels[number % 5]
        else:
            funny_word += consonants[number % 19]
    return funny_word


with open('test.txt') as data_file:
    N, x0 = map(int, data_file.readline().strip().split())
    word_length_list = map(int, data_file.readline().split())
    # From problem statement: for LCG A = 445, C = 700001, M = 2097152
    random_params = [445, 700001, 2097152, x0, sum(word_length_list)]
    random_gen = prob25.lcg_random(random_params)
    for word_length in word_length_list:
        random_numbers = []
        for num in range(word_length):
            random_numbers.append(next(random_gen))
        print funny_word_generator(random_numbers),

