def nth_random_finder(parameters):
    print parameters
    a = parameters[0]
    c = parameters[1]
    m = parameters[2]
    xnext = parameters[3]
    n = parameters[4]
    for k in range(n):
        xnext = (a * xnext + c) % m
    return xnext


def lcg_random(parameters):
    a = parameters[0]
    c = parameters[1]
    m = parameters[2]
    xnext = parameters[3]
    n = parameters[4]
    for k in range(n):
        xnext = (a * xnext + c) % m
        yield xnext


if __name__ == "__main__":
    inp = open('test.txt', 'r')
    N = int(inp.readline())
    for k in range(N):
        parameters = map(int, inp.readline().split())
        print nth_random_finder(parameters)
