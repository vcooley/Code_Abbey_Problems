"""
Integer Factorization
Represent an integer as the product of primes
"""

__author__ = 'Vince'

import prob61

def factorize(num):
    """
    Represents an integer as a list of its prime factors
    :param num:
    :return factors:
    """
    factors = []
    while num not in primes_list:
        for prime in primes_list:
            if num % prime == 0:
                factors.append(prime)
                num /= prime
                break
    factors.append(num)
    factors = sorted(factors)
    return factors

if __name__ == "__main__":
    primes = prob61.Primes()
    primes.prime_gen()
    primes_list = primes.prime_list
    with open("test.txt") as data_file:
        N = int(data_file.readline())
        for line in data_file:
            print "*".join(map(str, factorize(int(line)))),
