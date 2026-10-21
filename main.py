'''
    main.py
    orchestration-
    menus, prompts and printing
'''
import random
from board import Board
from ai import Human, easyAI, hardAI
from game import Game

def get_game_mode():
    '''
        gets game mode from user
    '''
    while True:
        player_mode = input('enter number of players between 1-2 (single vs AI, two player): ').strip()
        if player_mode in ('1', '2'):
            return int(player_mode)
        print('invalid choice. enter 1 or 2')

def get_ai_difficulty():
    '''
        gets ai difficulty from user
    '''
    while True:
        choice = input(
            "Choose computer difficulty:\n""1. easy\n""2. hard\n""enter 1 or 2: ").strip()
        if choice == "1":
            return easyAI
        elif choice == "2":
            return hardAI

        print("invalid choice. enter 1 or 2.")

def main():
    board = Board()
    rng = random.Random()
    player1 = Human(rng)
    print('this is tic tac toe')
    game_mode = get_game_mode()

    if game_mode == 2:
        player2 = Human(rng)
    else:
        ai_type = get_ai_difficulty()
        player2 = ai_type(rng)

    game = Game(board, 0, player1, player2)


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
