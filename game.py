'''
    game.py
    main game engine -
    turns, modes and win/lose checks
'''

class Game:
    def __init__(self, board, turn, player1, player2):
        self.board = board
        self.turn = turn
        self.player1 = player1
        self.player2 = player2

    def check_turn(self, turn):
        '''
            checks player1 or player2 turn
            returns true on p1 and false on p2
        '''
        return (turn % 2 == 0)


    def check_winner(self):
        '''
            checks for a winner
        '''
        return find_winner(self.board)

    def check_draw(self):
        '''
            checks for a draw
        '''
        return self.board.is_full() and self.check_winner() is None

    def play_turn(self):
        '''
            lets a player play their turn
        '''
        if self.check_turn(self.turn):
            mark = 'X'
            player = self.player1
        else:
            mark = 'O'
            player = self.player2
        while True:
            row, col = player.choose_move(self.board, mark)
            if self.board.place_mark(row, col, mark):
                break

        self.turn += 1

def find_winner(board):
    '''
        finds the winner
        defined at module level for reuse outside of game
    '''
    size = board.size
    lines = []
    #rows
    for row in range(size):
        temp = []
        for col in range(size):
            temp.append(board.cell(row, col))
        lines.append(temp)

    #col
    for col in range(size):
        temp = []
        for row in range(size):
            temp.append(board.cell(row, col))
        lines.append(temp)

    #diag
    temp = []
    for i in range(size):
        temp.append(board.cell(i, i))
    lines.append(temp)
    temp = []
    for i in range(size):
        temp.append(board.cell(i, size-1-i))
    lines.append(temp)

    # winning line
    for line in lines:
        if line[0] != ' ' and all(mark == line[0] for mark in line):
            return line[0]

    return None
