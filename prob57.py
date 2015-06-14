__author__ = 'Vince'

def smoother(rough_list):
    """
    Smoothes a list by averaging each value with the previous and next values
    :param rough_list:
    :return smooth_list:
    """
    smooth_list = [rough_list[0]]
    for idx in range(1, len(rough_list) - 1):
        smooth_val = sum(rough_list[idx - 1: idx + 2]) / 3.0
        smooth_list.append(smooth_val)
    smooth_list.append(rough_list[len(rough_list) - 1])
    return smooth_list

DATA = "test.txt"
with open(DATA) as data:
    N = int(data.readline())
    rough = map(float, data.readline().split())
for item in smoother(rough):
    print item,
