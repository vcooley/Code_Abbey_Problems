input_file = open('test.txt')
N = int(input_file.readline())
char_lines = input_file.readlines()
finally_list = []
how_many_list = []

for num in range(len(char_lines)):
	chars = char_lines[num].strip()
	finally_list.append(chars)
		

#Takes list of characters and checks for vowels.
def vowel_check(char_list):
	vowel_count = 0
	for num in range(len(char_list)):
		char = char_list[num]
		if char in ('a', 'e', 'i', 'o', 'u', 'y'):
			vowel_count += 1
	return vowel_count
	
for num in range(N):
	characters = list(finally_list[num])
	num_vowels = vowel_check(characters)
	how_many_list.append(num_vowels)
	
for num in range(N):
	print how_many_list[num],

