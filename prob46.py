__author__ = 'Vince'
"""Tic Tac Toe"""

from itertools import combinations

class TicTacToe(object):

    def __init__(self):
        self.x_list = []
        self.o_list = []
        self.moves = 0

    def reset(self):
        """I'm not sure if it's possible and/or pythonic to rerun __init__,
        so this function will simply reset the game.
        """
        self.x_list = []
        self.o_list = []
        self.moves = 0

    def game_is_won(self, player_list):
        """Pass this function x_list or o_list to check if that player won."""
        win_conditions = [
            (1, 2, 3),
            (4, 5, 6),
            (7, 8, 9),
            (1, 4, 7),
            (2, 5, 8),
            (3, 6, 9),
            (1, 5, 9),
            (3, 5, 7)
            ]
        player_list = sorted(player_list)
        for item in combinations(player_list, 3):
            # Creates a sorted list of all combinations of players owned spaces.
            if item in win_conditions:
                return True
        return False

    def move(self, player, placement):
        """Checks if move is valid, if it is, appends the placement (tile) to
         player's list. Then checks if that player won.
        """
        if placement in self.x_list or placement in self.o_list:
            print "Bad move. Try again."
        elif player.lower() == 'x':
            self.x_list.append(placement)
            self.moves += 1
        elif player.lower() == 'o':
            self.o_list.append(placement)
            self.moves += 1
        else:
            print "Something went wrong."

    def play(self, moveset):
        """Plays the game with the given moveset. Starts with X then
        alternates between player turns. Returns the move on
        which the game is won.
        """
        won = False
        self.reset()
        for indx in range(len(moveset)):
            current = int(moveset[indx])
            if indx % 2 == 0:
                self.move('x', current)
                won = self.game_is_won(self.x_list)
            else:
                self.move('o', current)
                won = self.game_is_won(self.o_list)
            if won:
                return self.moves
        return 0

inp = open('test.txt')
games = int(inp.readline())
a_game = TicTacToe()
for i in range(games):
    print a_game.play(inp.readline().split()),

inp.close()
