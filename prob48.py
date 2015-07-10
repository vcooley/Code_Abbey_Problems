"""This is a program to find out how many steps it takes to reach one using
a Collatz Sequence. In a Collatz Sequence, if a number is even, then the
next value is the result of dividing the number by two. Otherwise, the
next value is found by multiplying by 3 and adding one.
"""

def find_steps(value):
    """Counts how long it takes to reach one and loop."""
    count = 0
    sequence = [value]
    while value != 1:
        if value % 2 == 0:
            value /= 2
            sequence.append(value)
        else:
            value = value * 3 + 1
            sequence.append(value)
        count += 1
    return count, sequence

if __name__ == "__main__":
    inp = open('test.txt')
    N = int(inp.readline())
    starting_values = inp.readline().split()
    for val in starting_values:
        print find_steps(int(val)),
    inp.close()