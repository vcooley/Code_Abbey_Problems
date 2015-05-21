precision = 0.000000001

#Approximates square root using Babylonian method
#Kinda imprecise cause that's what Code Abbey wanted
#to make more precise, change to this
"""def sqrt_approx(v, pres):
	guess = 1.0
	rd_diff = 1.0
	d = guess
	while rd_diff > prec:
		guess = (guess + d) / 2.0
		d = v / guess
		rd_diff = abs(guess - d)
		
	return guess"""
def sqrt_approx(v, step):
	guess = 1.0
	rd_diff = 1.0
	d = guess
	for num in range (0, step + 1):
		guess = (guess + d) / 2.0
		d = v / guess
		rd_diff = abs(guess - d)
		
	return guess
	
inp = open('test.txt','r')
N = int(inp.readline())
for num in range(N):
	sqrtnum = inp.readline().split()
	approx = sqrt_approx(float(sqrtnum[0]), int(sqrtnum[1]))#change "int(sqrtnum[1])" to desired precision value
	print approx,
		