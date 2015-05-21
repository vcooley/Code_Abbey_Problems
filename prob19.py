def bracket_check(check_str):
	"""
	Takes a string and checks for bracket validity 
	by removing all other characters
	from the string and eliminating adjacent 
	pairs of corresponding open and close brackets.
	Returns 1 for valid brackets and 0 for invalid brackets.
	"""
	brackets = ['[' , ']' , '(' ,')', '{', '}', '<', '>']
	open_brackets = ['[', '(', '{', '<']
	close_brackets = [']', ')', '}', '>']
	bracket_map = {}
	
	for num in range(len(open_brackets)):
		bracket_map[close_brackets[num]] = open_brackets[num]
	str_list = list(check_str)
	check_all = []
	validity = 1
	k = 0
	#for loop to remove all characters except brackets.
	for num in range(len(str_list)):
		if str_list[num] in brackets:
			check_all.append(str_list[num])
	if len(check_all) % 2 != 0:#If not even number of brackets, validity = 0
		validity = 0 
	while k <= len(check_all) and validity == 1:
		#Checks for a close bracket at beginning or open bracket at end of list.
		if check_all == []:
			break
		elif check_all[0] in close_brackets:
			validity = 0
			break
		elif check_all[len(check_all) - 1] in open_brackets:
			validity = 0
			break
		if check_all[k] in close_brackets:
			if check_all[k - 1] == bracket_map[check_all[k]]:
				del check_all[k]
				del check_all[k - 1]
				k -= 1
			else:
				validity = 0
				break
		else:
			k += 1
		
	if check_all != []:
		validity = 0
	return validity

inp = open('test.txt', 'r')
N = int(inp.readline())
for num in range(N):
	print bracket_check(inp.readline()),
