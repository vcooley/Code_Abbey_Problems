"""
Prime Ranges.
Given a pair of prime numbers, find the number of primes in that range (inclusive).
"""

__author__ = 'Vince'

import prob61


class PrimesInRange(prob61.Primes):

    def primes_in_range(self, min_prime, max_prime):
        min_idx = self.prime_list.index(min_prime)
        max_idx = self.prime_list.index(max_prime)
        return max_idx - min_idx + 1

def main():
    primes_range = PrimesInRange(220000)
    primes_range.prime_gen()
    with open('test.txt') as data:
        N = int(data.readline())
        for i in range(N):
            prime_vals = map(int, data.readline().split())
            print primes_range.primes_in_range(prime_vals[0], prime_vals[1]),

if __name__ == "__main__":
    main()