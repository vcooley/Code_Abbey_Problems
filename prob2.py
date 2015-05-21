input = open('test.txt')
N = int(input.readline())
numbers = input.readline()
list = numbers.split(' ')
sum = 0
count = 0

for num in range(0,N):
	
	num = int(list[count])
	sum += num
	count +=1
	
print sum
