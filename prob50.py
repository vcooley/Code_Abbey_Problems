__author__ = 'Vince'

from string import punctuation

def palindrome_finder(phrase):
    """Checks if a string is a palindrome or not"""
    char_list = phrase.lower().strip().translate(None, punctuation)\
        .translate(None, " ")
    if char_list[::-1] == char_list:
        return "Y"
    else:
        return "N"

inp = open('test.txt')
N = int(inp.readline())
for i in range(N):
    phrase = inp.readline()
    print palindrome_finder(phrase),

inp.close()