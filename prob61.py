
from math import sqrt


class Primes(object):
    """
    Class that generates a list of primes.
    """
    def __init__(self):
        self.prime_list = [2]
        self.current_num = 3
        self.num_primes = 200000
    
    def prime_check(self, check_val):
        """
        Checks if a value is prime given a list of primes up until that value.
        param :prime_list: list of all primes < check_val
        param :check_val: value to check
        """
        # Assume value is prime until shown otherwise.
        is_prime = True
        for prime in self.prime_list:
            if check_val % prime == 0:
                is_prime = False
                break
            else:
                if sqrt(check_val) < prime:
                    break
        return is_prime

    def prime_gen(self):
        """
        Generates the first 200,000. Takes the optional kwarg last_check to change
        the number of primes to generate.
        """
        while len(self.prime_list) < self.num_primes:
            if self.prime_check(self.current_num):
                self.prime_list.append(self.current_num)
            self.current_num += 2        # Ensure number is always odd.
        

if __name__ == "__main__":
    primes = Primes()
    primes.prime_gen()

    with open('test.txt') as data_file:
        N = int(data_file.readline())
        prime_idxs = map(int, data_file.readline().split())
        for idx in prime_idxs:
            print primes.prime_list[idx - 1],
    