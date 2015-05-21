def find_GCD(A, B):
	max = A
	if B > A:
		max = B
		B = A
		A = max
	while B != 0:
		M = B
		B = A % M
		A = M
	return A

def find_LCM(A, B, GCD):
	LCM = (A * B) / GCD
	return LCM
	
inp = open('test.txt', 'r')
N = int(inp.readline())
for i in range(N):
	AandB = map(int, inp.readline().split())
	A = AandB[0]
	B = AandB[1]
	GCD = find_GCD(A, B)
	print "(%d %d)" % (GCD, find_LCM(A, B, GCD)), 