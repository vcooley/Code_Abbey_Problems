
PATH = "C:\Users\Sara\Documents\Random Vince Stuff\\test.txt"

def distance_finder(distance_speed):
    """
    Takes a list [distance between two cities, speed 1, speed 2] and returns
    the distance that the two travelers meet with respect to the first city.
    """
    distance = distance_speed[0]
    total_speed = distance_speed[1] + distance_speed[2]
    travel_time = float(distance) / total_speed
    distance_from_city1 = distance_speed[1] * travel_time
    return distance_from_city1
    
with open(PATH) as data_file:
    N = int(data_file.readline())
    for line in range(N):
        data = map(int, data_file.readline().split())
        print distance_finder(data),