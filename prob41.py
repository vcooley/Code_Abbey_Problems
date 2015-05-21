input_file = open('test.txt', 'r')
N = int(input_file.readline())
str_list = input_file.read()
num_list = str_list.split()
med_list = []
count = 0

def median(a, b, c):
	med = a
	if (a > b and a > c) or (a < c and a < b):
		med = b
		if (b > a and b > c) or (b < a and b < c):
			med = c
	return med
	
for num in range (0, N):
	count = 3 * num
	a = int(num_list[count])
	b = int(num_list[count + 1])
	c = int(num_list [count + 2])
	med = median(a, b, c)
	med_list.append(med)
	print a, b, c
	print med
	
for num in range(len(med_list)):
	print med_list[num],
	
