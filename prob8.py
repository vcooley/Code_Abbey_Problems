#splits a file into list that contains a list of strings in a line.
def splitlist():
	mylist = []
	
	for line in open('test.txt', 'r'):
		mylist.append(line.strip().split())
	return mylist
	
mylist = splitlist()

Nlist = mylist[0]
N = int(Nlist[0])

#Converts mylist into smaller lists then finds the arithmetic progression to do for each one
for num in range(1, N + 1):
	proglist = mylist[num]
	a1 = int(proglist[0])
	step = int(proglist[1])
	howmany = int(proglist[2])
	sum = 0
	for num in range(howmany):
		sum += a1 + num * step
	print sum,