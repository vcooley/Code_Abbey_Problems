"""
Fibonacci Divisibility
Given a value, m, find the index of the first fibonacci number evenly divisible by m.
"""

__author__ = 'Vince'


class FibonacciMethods(object):

    def __init__(self):
        self.fib_sequence = []
        self.fib_generator = self.fib_gen()
        self.more_fib_vals()

    def more_fib_vals(self):
        for i in range(500):
            self.fib_sequence.append(self.fib_generator.next())

    def fib_gen(self):
        """
        Fibonacci sequence generator.
        """
        a, b = 0, 1
        while True:
            yield a
            a, b = b, a + b

    def fib_divide(self, val):
        """
        Looks for the first fibonacci number evenly divisible by val.
        Generates more fibonacci numbers if no current ones are divisible by val.
        :param val:
        :return:
        """
        for idx, number in enumerate(self.fib_sequence):
            if number == 0:
                continue
            if number % val == 0:
                return idx
        self.more_fib_vals()
        return self.fib_divide(val)


def main():
    with open('test.txt') as data_file:
        N = int(data_file.readline())
        m_values = map(int, data_file.readline().strip().split())
        fib_stuff = FibonacciMethods()
        for val in m_values:
            print fib_stuff.fib_divide(val),

if __name__ == "__main__":
    main()