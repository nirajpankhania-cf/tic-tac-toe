
import pytest
import random
from board import Board
from game import Game, find_winner
from ai import easyAI

rng = random.Random()

def make_board(rows):
    board = Board(len(rows))

    for r, row in enumerate(rows):
        for c, mark in enumerate(row):
            if mark != ' ':
                board.place_mark(r,c,mark)
    return board

@pytest.mark.parametrize(
    ('rows', 'expected'),
    [
        (["XXX","OO ","   "], 'X'), #rows
        (["X O", "X O", "  O"], 'O'), # cols
        (["XO ", " XO", "  X"], 'X'), #diag1
        (['  X', "OX ", "XO "], 'X'), #diag2
    ],
)
def test_detect_winner_in_every_direction(rows, expected):
    board = make_board(rows)
    assert find_winner(board) == expected

def test_full_board_no_winner_is_draw():
    board = make_board(
        ["XOX","XOX","OXO"]
    )
    game = Game(board, 0, None, None)
    assert find_winner(board) is None
    assert game.check_draw() == True

def test_x_plays_first():
    board = Board()
    player = easyAI(rng)

    game = Game(board, 0, player, None)
    game.play_turn()
    assert len(board.empty_cells()) == 8
    for r in range(3):
        for c in range(3):
            if board.cell(r,c) != ' ':
                assert board.cell(r,c) == 'X'
