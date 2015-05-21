def loop_check(v):
	loop_check = [v]
	count = 0
	while True:
		v = v * v
		v /= 100
		v %= 10000
		count += 1
		if v in loop_check:
			break
		loop_check.append(v)
	return count

inp = open('test.txt', 'r')
N = int(inp.readline())
pseudo = map(int, inp.readline().split())
print pseudo
for k in range(len(pseudo)):
	print loop_check(pseudo[k]),
	
