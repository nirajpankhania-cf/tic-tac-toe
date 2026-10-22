import pytest

import random
from ai import Human, hardAI, easyAI
from board import Board
from game import Game
from test_game import make_board

rng = random.Random()

def test_choose_move_does_not_affect_board():
    board = Board()
    player1, player2 = easyAI(rng), easyAI(rng)

    game = Game(board, 0, player1, player2)
    player1.choose_move(board, 'X')
    player2.choose_move(board, 'O')
    assert len(board.empty_cells()) == 9

def test_easy_returns_empty_cell():
    board = Board()
    player1, player2 = easyAI(rng), easyAI(rng)

    r,c = (player1.choose_move(board, 'X'))
    assert board.cell(r,c) == ' '

def test_hard_chooses_winning_move():
    board = make_board(
        ["OXO","OXO","X  "]
    )
    player1 = hardAI(rng)

    r,c = player1.choose_move(board, 'O')
    board.place_mark(r,c,'O')

    game = Game(board, 0, None, None)
    assert game.check_winner() == 'O'
