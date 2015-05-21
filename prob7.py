infile = open('test.txt')
str = infile.read()
list = str.split()
print list

#convert list to floating point numbers
def floating_list(list):
	float_list = []
	for num in range(len(list)):
		floatnum = float(list[num])
		float_list.append(floatnum)
	return float_list
	
#Rounds numbers in a floating point list and converts to integer
def round_to_int(float_list):
	int_list = []
	for num in range(len(float_list)):
		int_num = int(round(float_list[num]))
		int_list.append(int_num)
	return int_list
	
change_list = floating_list(list)


N = int(change_list[0])
round_list = []

for num in range(1, N + 1):
	F_value = change_list[num]
	C_value = (F_value - 32) * (5.0 / 9.0)
	round_list.append(C_value)
	
final_list = round_to_int(round_list)
for num in range(len(final_list)):
	print final_list[num],


