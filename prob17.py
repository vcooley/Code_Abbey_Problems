input_file = open('test.txt', 'r')
N = int(input_file.readline())
string = input_file.readline()
check_array = map(int, string.split())
result = 0
for num in range (len(check_array)):
	result += check_array[num]
	result *= 113
	result %= 10000007
print result