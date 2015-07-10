"""
Selection Sort
"""

__author__ = 'Vince'

def selection_sort(num_list):
    """
    Uses a selection sort algorithm to return an sorted array (min to max).
    :param num_list:
    :return sorted_list:
    """
    N = len(num_list)
    sorted_list = []
    max_indices = []
    while N > 1:
        largest_idx = 0
        max_val = num_list[largest_idx]
        for idx in range(N):
            if num_list[idx] > max_val:
                max_val = num_list[idx]
                largest_idx = idx
        temp = num_list[N - 1]
        num_list[N - 1] = num_list[largest_idx]
        num_list[largest_idx] = temp
        max_indices.append(largest_idx)
        N -= 1
    return max_indices


with open('test.txt') as data_file:
    data_file.readline()
    numbers = map(int, data_file.readline().split())
    indices = selection_sort(numbers)
    for item in indices:
        print item,

