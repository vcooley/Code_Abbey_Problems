input_file = open('test.txt', 'r')
N = int(input_file.readline())

while True:
	op_num = input_file.readline().split()
	if op_num[0] == '+':
		N += int(op_num[1])
	elif op_num[0] == '*':
		N *= int(op_num[1])
	elif op_num[0] == '%':
		N %= int(op_num[1])
		break
	else:
		exit(1)
print N