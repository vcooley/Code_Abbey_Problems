input_file = open('test.txt', 'r')
N = int(input_file.readline())
num_list = input_file.readline().split()

#Breaks integer into list of digits. Returned list begins with the leftmost digit.
def brk_dig(num):
	dig_list = []
	while num != 0:
		dig = num % 10
		dig_list.insert(0, dig)
		num /= 10
	return dig_list
	
for num in range(N):
	big_num = int(num_list[num])
	dig_list = brk_dig(big_num)
	wsd = 0
	for k in range(len(dig_list)):
		wsd += (k + 1) * dig_list[k]
	print wsd,