#splits a file into list that contains a list of strings in a line.
def splitlist():
	mylist = []
	
	for line in open('test.txt', 'r'):
		mylist.append(line.strip().split('\n'))
	return mylist

#Finds the number to break into digits
#k is the instance to find
def findnum(numlist, k):
	numbers = numlist[k]
	str_list = numbers[0].split()
	a, b , c = int(str_list[0]), int(str_list[1]), int(str_list[2])
	num = a * b + c
	return num

#Returns num % 10 and num / 10
def breakdigit(num):
	digit = num % 10
	next = num /10
	return digit, next
	
mylist = splitlist()
Nlist = mylist[0]
N = int(Nlist[0])

for num in range(1, N + 1):
	next = findnum(mylist, num)
	sum = 0
	while next != 0:
		digit, next = breakdigit(next)
		sum += digit
	print sum,
		

