__author__ = 'Vince'

"""Given a value, find it's index in the Fibonacci Sequence. 0 is the
0th index, 1 the 1st, 1 the 2nd, etc. Code Abbey states that no index will
be larger than 1000.
"""


class Fib_Finder(object):

    def __init__(self, seq_length=1000):
        self.fib_index = seq_length
        self.fib_sequence = self.create_fib()

    def create_fib(self):
        """Creates a list from the Fibbonaci Sequence of fib_index values."""
        fib_list = [0, 1, 1]
        for i in range(2, self.fib_index):
            fib_list.append(fib_list[i] + fib_list[i - 1])
        return fib_list

    def find_fib_index(self, value):
        """Finds the index for the given value falls in the Fibonacci Sequence."""
        min_indx = 0
        max_indx = len(self.fib_sequence)
        guess = (min_indx + max_indx) / 2
        while self.fib_sequence[guess] != value:
            if value > self.fib_sequence[guess]:
                min_indx = guess
            else:
                max_indx = guess
            guess = (min_indx + max_indx) / 2
        return guess


index_finder = Fib_Finder()
inp = open('test.txt')
N = int(inp.readline())
for i in range(N):
    number = int(inp.readline())
    print index_finder.find_fib_index(number),
