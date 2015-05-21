#splits a file into list that contains a list of strings in a line.
def splitlist():
	mylist = []
	
	for line in open('test.txt', 'r'):
		mylist.append(line.strip().split())
	return mylist

#Finds (possible) hypotenuse given three values	
def hypfinder(a, b, c):
	max = a
	if b > max:
		max = b
		b = a
	if c > max:
		t = c
		c = max
		max = t
	return max, b, c
		
mylist = splitlist()
Nlist = mylist[0]
N = int(Nlist[0])

for num in range(1, N + 1):
	trilist = mylist[num]
	
	x, y, z = int(trilist[0]), int(trilist[1]), int(trilist[2])
	
	hyp, a, b = hypfinder(x, y, z)
	if a + b >= hyp:
		print 1,
	else:
		print 0,
	

