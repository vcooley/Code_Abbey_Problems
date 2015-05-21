input = open('test.txt', 'r')
list = input.read()
string_list = list.split()
newlist = map(int, string_list)

N = len(newlist)
max = newlist[0]
min = newlist[0]



#Finds max number in newlist
for num in range(0, N):
	if newlist[num] > max:
		max = newlist[num]
	

#Finds min number in newlist		
for num in range(N):
	if newlist[num] < min:
		min = newlist[num]

		
print max, min
	
	
