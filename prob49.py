__author__ = 'Vince'
"""Rock Paper Scissors"""

def rps(moveset):
    """Moveset should be list of strings such as RS, SR, PP representing
    the first and second players moves. Function counts who wins
    most games and returns the winner (1 or 2).
    """
    player_one_wins = 0
    player_two_wins = 0
    for game in moveset:
        if game[0] == game[1]:
            continue
        elif game[0] == 'R':
            if game[1] == 'S':
                player_one_wins += 1
            else:
                player_two_wins += 1
        elif game[0] == "S":
            if game[1] == "P":
                player_one_wins += 1
            else:
                player_two_wins += 1
        else:
            if game[1] == "R":
                player_one_wins += 1
            else:
                player_two_wins += 1
    if player_one_wins > player_two_wins:
        return 1
    elif player_two_wins > player_one_wins:
        return 2
    else:
        return "draw"

inp = open('test.txt')
N = int(inp.readline())
for i in range(N):
    print rps(inp.readline().split()),
inp.close()