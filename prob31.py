inp = open('test.txt', 'r')
N = int(inp.readline())

def char_switch(char_list, k):
    if k > 0:
        for i in range(k):
            char_list.append(char_list.pop(0))
    else:
        i = -1
        while i >= k:
            char_list.insert(0, char_list.pop(len(char_list)- 1))
            i -= 1
    return char_list


for k in range(N):
    characters = list(inp.readline().replace(" ", "").replace("\n", ""))
    if characters[0] == '-':
        characters.pop(0)
        k = int(characters.pop(0)) * -1
    else:
        k = int(characters.pop(0))
    reordered = char_switch(characters, k)
    print "".join(reordered),

