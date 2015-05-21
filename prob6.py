infile = open('test.txt', 'r')
N = int(infile.readline())

list = []

for line in infile:
	list.append(line.strip())
	
for num in range(N):	
	pair = list[num].split()
	a = float(pair[0])
	b = float(pair[1])
	result = a / b
	rounded = int(round(result))
	print rounded,
