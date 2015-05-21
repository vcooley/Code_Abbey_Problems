inp = open('test.txt')
array = map(int, inp.readline().split())
print array

for i in range(len(array)):
	if array[i] = -1:
		break
	k = array[i]
	h = array[i + 1]
	if h < k:
		array[i] = h
		array[i + 1] = k