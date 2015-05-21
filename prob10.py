#splits a file into list that contains a list of strings in a line.
def splitlist():
	mylist = []
	
	for line in open('test.txt', 'r'):
		mylist.append(line.strip().split('\n'))
	return mylist

mylist = splitlist()
Nlist = mylist[0]
N = int(Nlist[0])

for i in range(1, N + 1):
	points = mylist[i]
	npoints = points[0].split()
	x1, y1, x2, y2 = int(npoints[0]), int(npoints[1]), int(npoints[2]), int(npoints[3])
	a = (y1 - y2)/(x1 - x2)
	b = y1 - a * x1
	print "(%d %d)" % (a, b),
