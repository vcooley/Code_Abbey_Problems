"""
Combinations Counting
"""

__author__ = 'Vince'

def n_choose_k(n, k):
    """
    Function that returns the number of choices, k, of a set of length n.
    :param n:
    :param k:
    :return combinations:
    """
    n_min_k = n - k
    combinations = 1
    while n > 1:
        combinations *= 1
        n -= 1
    while k > 1:
        combinations /= k
        k -= 1
    while n_min_k > 1:
        combinations /= n_min_k
        n_min_k -= 1
    return combinations


with open('test.txt') as data_file:
    N = int(data_file.readline())
    for case in range(N):
        n_k_vals = map(int, data_file.readline().split())
        print n_choose_k(n_k_vals[0], n_k_vals[1]),
