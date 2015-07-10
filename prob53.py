"""
King and Queen.
Given a king and queen position on a chess board, check whether the king is in check.
"""

__author__ = 'Vince'

from math import fabs

def check_for_check(k_position, q_position):
    k_position = list(k_position)
    q_position = list(q_position)
    k_position[0] = ord(k_position[0].lower()) - 96
    q_position[0] = ord(q_position[0].lower()) - 96
    if k_position[0] == q_position[0] or k_position[1] == q_position[1]:
        return "Y"
    else:
        x_diff = int(k_position[0]) - int(q_position[0])
        y_diff = int(k_position[1]) - int(q_position[1])
        if fabs(x_diff) == fabs(y_diff):
            return "Y"
    return "N"

with open('test.txt') as f:
    N = int(f.readline())
    for i in range(N):
        positions = f.readline().split()
        k = positions[0]
        q = positions[1]
        print(check_for_check(k, q)),
