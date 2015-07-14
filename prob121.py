"""
Insertion Sort

"""

__author__ = 'Vince'


class InsertionSort(object):
    """
    Contains an array and the methods to sort it by insertion sort.
    """
    def __init__(self, initial_value):
        self.sorted_array = [initial_value]

    def find_index(self, value):
        """
        Return the index where the value should be located.
        :param value:
        :return:
        """
        for idx, number in enumerate(self.sorted_array):
            if number > value:
                return idx
        return len(self.sorted_array)

    def insertion_sort(self, new_value):
        """
        Insert a value into its correct position in an array.
        :param new_value:
        :return:
        """
        index = self.find_index(new_value)
        print len(self.sorted_array) - index,  # Answer output for CodeAbbey
        self.sorted_array.insert(index, new_value)


def main():
    with open('test.txt') as data_file:
        N = int(data_file.readline())
        unsorted_array = map(int, data_file.readline().split())
        list_sorter = InsertionSort(unsorted_array.pop(0))
        for value in unsorted_array:
            list_sorter.insertion_sort(value)

if __name__ == "__main__":
    main()