
"""
Bit count
"""

PATH = 'test.txt'

def count_bits(int_value):
    """
    Counts the number of bits in an integer.
    :param int_value:
    :return bit_count:
    """
    bit_count = 0
    if int_value < 0:
        bin_value = neg_int_to_bit(int_value)
    else:
        bin_value = int_value
    bin_list = list(bin(bin_value))
    for bit in bin_list:
        if bit == '1':
            bit_count += 1
    return bit_count


def neg_int_to_bit(int_value, bit_size=32):
    """
    Converts a negative integer to its 2's complement binary form.
    Standard bit count is 32.
    :param int_value:
    :param bit_size:
    :return bin_value:
    """
    mask = 0
    for bit in range(bit_size):
        mask += 2 ** bit
    bin_value = mask ^ int_value + 1
    print bin(int_value)
    print bin(bin_value)
    return bin_value


with open(PATH) as data_file:
    N = int(data_file.readline())
    for integer in data_file.readline().split():
        print count_bits(int(integer)),
"""
11111111111111111111111111111111
00000000000000000000001000101000
11111111111111111111110111010111

11111111111111111111111111111111
00000000000000000000000101010001
11111111111111111111111010101111
"""
