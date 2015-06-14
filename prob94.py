"""
Fool's Day 2014
Solve the problem without the problem statement.
"""

__author__ = 'Vince'

def sum_of_squares(num_list):
    sum_squares = 0
    for val in num_list:
        sum_squares += val ** 2
    return sum_squares


with open('test.txt') as data_file:
    trials = int(data_file.readline())
    for trial in range(trials):
        sum_vals = map(int, data_file.readline().split())
        print sum_of_squares(sum_vals),



