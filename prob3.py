input = open('test.txt')
N = int(input.readline())
list = []


for num in range(0, N):
	
	numbers = input.readline()
	pair = numbers.split(' ')
	sum = int(pair[0]) + int(pair[1])
	list.append(sum)

for num in range(0, N):
	print list[num],
	

