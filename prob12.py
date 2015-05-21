def findlist(numlist, k):
	numbers = numlist[k]
	str_list = numbers[0].split()
	int_list = []
	for num in range(len(str_list)):
		int_list.append(int(str_list[num]))
	return int_list

#splits a file into list that contains a list of strings in a line.
def splitlist():
	mylist = []
	for line in open('test.txt', 'r'):
		mylist.append(line.strip().split('\n'))
	return mylist

#takes time in days, hours, minutes, seconds and converts to time in seconds
def find_sec(d, h, m, s):
	d_sec = d * 3600 * 24
	h_sec = h * 3600
	m_sec = m * 60
	sec_sum = d_sec + h_sec + m_sec + s
	return sec_sum

#Takes time in seconds and returns time in days, hours, minutes, seconds
def reg_time(time_sec):
	sec = time_sec % 60
	min = (time_sec / 60) % 60
	hour = (time_sec / 3600) % 24
	day = (time_sec / 86400)
	return day, hour, min, sec

	
mylist = splitlist()
Nlist = mylist[0]
N = int(Nlist[0])

for k in range (1, N + 1):
	timelist = findlist(mylist, k)
	time1 = find_sec(timelist[0], timelist[1], timelist[2], timelist[3])
	time2 = find_sec(timelist[4],timelist[5], timelist[6], timelist[7])
	diff_sec = time2 - time1
	day, hour, min, sec = reg_time(diff_sec)
	print "(%d %d %d %d)" % (day, hour, min, sec),