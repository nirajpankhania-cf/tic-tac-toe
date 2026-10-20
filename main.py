'''
    main.py
    orchestration-
    menus, prompts and printing
'''

from board import Board
from ai import Human
from game import Game

def main():
    board = Board()
    player1 = Human()
    player2 = Human()

    game = Game(board, 0, player1, player2)

    print('this is tic tac toe')
    print('player1 is "X" and player2 is "O"')

    while game.check_winner() is None and not game.check_draw():
        print(board)
        game.play_turn()

    print(board)
    winner = game.check_winner()

    if winner == 'X':
        print('Player1 wins!')
    elif winner == 'O':
        print('Player2 wins!')
    else:
        print('DRAW')

if __name__ == "__main__":
    main()
