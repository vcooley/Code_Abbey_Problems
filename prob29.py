inp = open('test.txt','r')
N = int(inp.readline())
array = map(int, inp.readline().split())
current_swaps = 'ten million'
positions = []

# creates list of positions. positions will be swapped along with values.
for k in range(N):
	positions.append(k + 1)
	
position_array_list = [array , positions]
print position_array_list

while current_swaps != 0:
	current_swaps = 0
	for k in range(len(array) - 1):
		if position_array_list[0][k] > position_array_list[0][k + 1]:
			t = position_array_list[0][k + 1]
			v = position_array_list[1][k + 1]
			
			position_array_list[0][k + 1] = position_array_list[0][k]
			position_array_list[1][k + 1] = position_array_list[1][k]
			
			position_array_list[0][k] = t
			position_array_list[1][k] = v
			
			current_swaps += 1

for k in range(len(position_array_list[1])):
	print position_array_list[1][k],