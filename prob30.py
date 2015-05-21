import sys

inp = "make about bulb cactus struggle pick stay"
char_list = list(inp)
N = len(char_list)
print N
for k in range(0, N / 2):
	t = char_list[N - k - 1]
	
	char_list[N - k - 1] = char_list[k]
	char_list[k] = t
	
for k in range(N):
	stuff = sys.stdout.write(char_list[k])
	
print stuff	
sys.stdout.flush()