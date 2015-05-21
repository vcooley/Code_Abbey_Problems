inp = open('test.txt')
array = map(int, inp.readline().split())
array.remove(-1)
swaps = 0
print array

#Bubble swap
for i in range(len(array) - 1):
	k = array[i]
	h = array[i + 1]
	if h < k:
		swaps += 1
		array[i] = h
		array[i + 1] = k

#Checksum
result = 0		
for num in range (len(array)):
	result += array[num]
	result *= 113
	result %= 10000007

print array
print swaps, result