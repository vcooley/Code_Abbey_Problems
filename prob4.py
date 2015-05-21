input = open('test.txt')
N = int(input.readline())
list = []


for num in range(0, N):
	
	numbers = input.readline()
	pair = numbers.split(' ')
	if int(pair[0]) > int(pair[1]):
		list.append(int(pair[1]))
	else:
		list.append(int(pair[0]))

for num in range(0, N):
	print list[num],
	

