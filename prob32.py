__author__ = 'Vince'
"""Josephus' problem"""

N = 99
k = 7
count = 1
index_count = 0
n_numbers = []


for i in range(1, N + 1):
    n_numbers.append(i)

print n_numbers
while len(n_numbers) > 1:
    if index_count >= len(n_numbers):
        index_count = 0
    if count == k + 1:
        del n_numbers[index_count - 1]
        if index_count != 0:
            index_count -= 1
        count = 1
        print index_count, n_numbers

    index_count += 1
    count += 1

print n_numbers[0]