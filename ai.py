'''
    ai.py
    for the ai and player classes
'''

import random
from abc import ABC, abstractmethod
from game import find_winner


class Player(ABC):
    def __init__(self, rng):
        self._rng = rng
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
    """
        Picks any empty cell at random.
    """

    def choose_move(self, board, mark):
        return self._rng.choice(board.empty_cells())

class hardAI(Player):
    '''
        minimax for optimal move on a 3x3 board
        If the game is over, return the score from X's perspective.
        Otherwise get a list of new game states for every possible move
        Create a scores list
        For each of these states add the minimax result of that state to the scores list
        If it's X's turn, return the maximum score from the scores list
        If it's O's turn, return the minimum score from the scores list
    '''

    def choose_move(self, board, mark):
        moves = board.empty_cells()
        if not moves:
            raise ValueError("no empty cells left")

        best_score = float("-inf")
        best_moves = []

        # try each move
        for row,col in moves:
            clone = board.copy()
            clone.place_mark(row, col, mark)

            # predict outcome after this move
            score = self._minimax(clone, self._opponent(mark), mark, False)

            # store the best score/scores
            if score > best_score:
                best_score = score
                best_moves = [(row, col)]
            elif score == best_score:
                best_moves.append((row, col))

        #choose randomly between the best moves
        return self._rng.choice(best_moves)

    def _minimax(self, board, current_mark, ai_mark, maxxing):
        #stop when game end
        winner = find_winner(board)
        if winner == ai_mark:
            return 1
        if winner == current_mark:
           return -1
        if board.is_full():
            return 0

        scores = []

        #simulate every move for curr player
        for row, col in board.empty_cells():
            clone = board.copy()
            clone.place_mark(row, col, current_mark)

            #switch players and continue
            score = self._minimax(clone, self._opponent(current_mark), ai_mark, not maxxing)
            scores.append(score)

        #opponent mins, ai max
        if maxxing:
            return max(scores)
        else:
            return min(scores)

    @staticmethod
    def _opponent(mark):
        return "O" if mark == "X" else "X"
