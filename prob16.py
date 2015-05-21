input_file = open('test.txt', 'r')
N = int(input_file.readline())

for num in range(N):
	avg_list = input_file.readline().split()
	sum = 0
	for k in range(len(avg_list)- 1):
		sum += float(avg_list[k])
	avg = sum / float(len(avg_list) - 1)
	print int(round(avg)),
		