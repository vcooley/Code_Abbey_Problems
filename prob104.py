"""
Triangle Area.
Solve area of a triangle given three points in a plane.
"""

__author__ = 'Vince'

from math import sqrt


def distance(p1, p2):
    """
    Finds the distance between two points
    :param p1:
    :param p2:
    :return dist:
    """
    dist = sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)
    return dist


def distance_finder(point_list):
    """
    Finds distance between each point given a list of points. Outputs a
    dictionary with key = point and value = dictionary with keys = all other
    points and values = distance to that point.
    :param point_list:
    :return distance_dict:
    """
    distance_dict = {}
    for point_idx, start_point in enumerate(point_list):
        distance_dict[point_idx] = {point_list.index(end_point):
                                    distance(start_point, end_point) for
                                    end_point in point_list
                                    if end_point != start_point
                                    }
    return distance_dict


def tri_area(point_list):
    """
    Given a list of three points, find the area of the triangle whose angles
    are at those three points.
    :param point_list:
    :return area:
    """
    # Compute the distances between the points given.
    distances = distance_finder(point_list)
    # Assign each unique distance to a leg a, b, or c.
    a = distances[0][1]
    b = distances[0][2]
    c = distances[1][2]
    # Use Heron's formula to find the area of a triangle.
    semi_perm = (a + b + c) / 2
    s = semi_perm    # Make next line more readable
    area = sqrt(s * (s - a) * (s - b) * (s - c))
    return area


def point_maker(pairwise_list):
    """
    Makes a list of points from a list of strings.
    :param pairwise_list:
    :return point_list:
    """
    point_list = []
    for pt_idx in range(0, len(pairwise_list), 2):
        x_val = float(pairwise_list[pt_idx])
        y_val = float(pairwise_list[pt_idx + 1])
        point_list.append((x_val, y_val))
    return point_list

with open('test.txt') as data_file:
    N = int(data_file.readline())
    for line in range(N):
        points = data_file.readline().split()
        points = point_maker(points)
        print tri_area(points),
