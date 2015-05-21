__author__ = 'Vince'

from math import sqrt

inp = open('test.txt')
out = open('result.txt', 'w')
N = int(inp.readline())

def std_dev(stock):
    """
    Find standard deviation of a stock.
    Input should be a list with the name of the stock
    followed by it's prices for some period of time.
    Will output name, mean, and std dev of stock in order
    to make a purchase decision about that stock.
    """
    name = stock[0]
    prices = map(float,stock[1:])
    psum = 0.0
    # Sum up the prices then find the mean
    for i in range(len(prices)):
        psum += prices[i]
    avg = psum / (len(prices))
    var = 0.0
    for i in range(len(prices)):
        # Find the variance and divide by number of items
        var += (prices[i] - avg) ** 2.0
    mdev = var / float(len(prices))
    stdev = sqrt(mdev)
    return name, avg, stdev

for i in range(N):
    # Get data and pass it to our std_dev function.
    stock_data = inp.readline().split()
    name, mean, deviation = std_dev(stock_data)
    # Lets make a decision. Std. deviation should be at least 4x
    # broker's cut (1%). for us to make a purchase.
    broker_cut = 0.01
    threshold = 4.0 * broker_cut * mean
    if deviation >= threshold:
        out.write("%s " % name)
