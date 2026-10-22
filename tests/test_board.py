import pytest
from board import Board

def test_new_board_size_is_three():
    board = Board()
    assert board.size == 3

def test_place_mark_rejects_out_of_range():
    board = Board()
    mark = 'X'

    assert board.place_mark(1,5, mark) == False

def test_place_mark_updates_board_correctly():
    board = Board()
    mark = 'X'

    assert board.place_mark(1,1, mark) == True
    assert board.cell(1,1) == 'X'

def test_place_mark_rejects_occupied_cell():
    board = Board()
    mark = 'X'

    board.place_mark(1,1,mark)
    assert board.place_mark(1,1,mark) == False


def test_new_board_is_empty():
    board = Board()

    assert board.size == 3
    assert board.is_full() is False
    assert len(board.empty_cells()) == 9
    assert all(board.cell(r,c) == ' ' for r in range(3) for c in range(3))

def test_copy_independent_of_original():
    board = Board()
    board.place_mark(1,1,'X')

    clone = board.copy()
    clone.place_mark(1,2,'O')

    assert board.cell(1,2) == ' '
    assert clone.cell(1,1) == 'X'
