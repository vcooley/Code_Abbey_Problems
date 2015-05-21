input = open('test.txt')
N = int(input.readline())
list = []

for num in range(0, N):
	numbers = input.readline()
	pair = numbers.split(' ')
	if int(pair[0]) > int(pair[1]):
		if int(pair[1]) < int(pair[2]):
			list.append(int(pair[1]))
		else:
			list.append(int(pair[2]))
	else:
		if int(pair[0]) < int(pair[2]):
			list.append(int(pair[0]))
		else:
			list.append(int(pair[2]))

for num in range(0, N):
	print list[num],
	
