inp = open('test.txt', 'r')
MN = inp.readline().split()
M = int(MN[1])
N = int(MN[0])


count_list = []
for k in range(M):
	count_list.append(0)


pre_list = inp.readline().split()
int_list = []
for k in range(len(pre_list)):
	number = int(pre_list[k])
	int_list.append(number)
	
for k in range(len(int_list)):
	i = int_list[k]
	count_list[i - 1] += 1

for k in range(len(count_list)):
	print count_list[k],