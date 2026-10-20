'''
    ai.py
    for the ai and player classes
'''

import random
from abc import ABC, abstractmethod


class Player(ABC):
    @abstractmethod
    def choose_move(self, board, mark)->tuple[int, int]:
        """Return a (row, col) tuple for an empty cell on the board."""


class Human(Player):
    '''
        prompts a human player to input a coordinate
    '''
    def choose_move(self, board, mark):
        while True:
            try:
                choice = input('choose a row and column e.g. "1 1": ').strip()
                row, col = choice.split()
                row, col = int(row), int(col)
                return row-1, col-1
            except ValueError:
                print("invalid input please try two integers e.g.'1 1'")

class easyAI(Player):
    """Picks any empty cell at random."""

    def __init__(self, rng=None):
        if rng is None:
            rng = random.Random()
        self._rng = rng

    def choose_move(self, board, mark):
        return self._rng.choice(board.empty_cells())
