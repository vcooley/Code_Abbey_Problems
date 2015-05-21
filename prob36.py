# Start by assuming all digits can be correct.
dig1_right = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
dig2_right = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
dig3_right = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
dig4_right = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']

inp = open('test.txt', 'r')
N = int(inp.readline())
some_correct = []


# For loop to eliminate bad values from candidate list.
for i in range(N):
    guess = list(inp.readline())
    print guess
    if int(guess[5]) == 0:
        if guess[0] in dig1_right:
            dig1_right.remove(guess[0])
        if guess[1] in dig2_right:
            dig2_right.remove(guess[1])
        if guess[2] in dig3_right:
            dig3_right.remove(guess[2])
        if guess[3] in dig4_right:
            dig4_right.remove(guess[3])

inp.seek(0)
inp.readline()

# For loop to check how many digits are correct and if the same amount remain in respective candidate list.
for i in range(N):
    guess = list(inp.readline())
    cor = int(guess[5])
    count = 0
    dig1 = False
    dig2 = False
    dig3 = False
    dig4 = False
    if guess[0] in dig1_right:
        count += 1
        dig1 = True
    if guess[1] in dig2_right:
        count += 1
        dig2 = True
    if guess[2] in dig3_right:
        count += 1
        dig3 = True
    if guess[3] in dig4_right:
        count += 1
        dig4 = True
    if count == cor:
        if dig1 == True:
            dig1_right = guess[0]
        if dig2 == True:
            dig2_right = guess[1]
        if dig3 == True:
            dig3_right = guess[2]
        if dig4 == True:
            dig4_right = guess[3]

print dig1_right, dig2_right, dig3_right, dig4_right