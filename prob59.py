"""
Bulls and Cows
Given a secret number and a series of guesses, print value such as 0-1 for
each guess, where the first value indicates the number of digits in the
correct position and the second value indicates the number of correct digits
in the incorrect position.
"""

__author__ = 'Vince'

def digit_checker(correct, guess):
    """
    Finds the total number of correct digits in the guess and the number of
    correct digits in the wrong place.
    :param correct:
    :param guess:
    :return :
    """
    correct = list(correct)
    guess = list(guess)
    correct_position = 0
    correct_digit = 0
    for idx, digit in enumerate(correct):
        if digit == guess[idx]:
            correct_position += 1
        elif guess[idx] in correct:
            correct_digit += 1
    return correct_position, correct_digit


with open('test.txt') as data_file:
    digit_N = data_file.readline().split()
    secret = digit_N[0]
    N = digit_N[1]
    guesses = data_file.readline().split()
    for val in guesses:
        print "%s-%s" % (digit_checker(secret, val)),
