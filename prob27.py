inp = open('test.txt','r')
N = int(inp.readline())
array = map(int, inp.readline().split())
current_swaps = 'ten million'
total_swaps = 0
passes = 0


while current_swaps != 0:
	current_swaps = 0
	for k in range(len(array) - 1):
		if array[k] > array[k + 1]:
			t = array[k + 1]
			array[k + 1] = array[k]
			array[k] = t
			current_swaps += 1
	total_swaps += current_swaps
	passes += 1
		
print passes, total_swaps