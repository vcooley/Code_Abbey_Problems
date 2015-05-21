__author__ = 'Vince'
"""Parity control"""

import sys

def check_encoding(binary_list):
    sum = 2 # Compensate if for loop returns sum of 1
    for k in range(len(binary_list)):
        sum += binary_list[k]
    check = sum % 2
    if check != 0:
        return 'corrupt'
    else:
        return 'ok'

def find_base10(binary_list):
    sum = 0
    for k in range(len(binary_list)):
        n = len(binary_list) - k - 1
        val = binary_list[k] * (2 ** n)
        sum += val
    return sum

inp = open('test.txt')
encoded_inp = map(int, inp.readline().split())
print encoded_inp

k = 0
decoded_ascii = []
while k < len(encoded_inp):
    bin_num = bin(encoded_inp[k])
    bin_list = list(bin_num)
    del bin_list[0], bin_list[0] # Delete 'b' in binary output
    bin_list = map(int, bin_list)
    while len(bin_list) < 8:
        bin_list.insert(0, 0)
    if check_encoding(bin_list) == 'corrupt':
        del encoded_inp[k]
    else:
        del bin_list[0]
        decoded_ascii.append(find_base10(bin_list))
        k += 1

message = []
for i in range(len(decoded_ascii)):
    message = sys.stdout.write(chr(decoded_ascii[i]))
print message



