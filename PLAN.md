**Goal**

This is a tic tac toe game that will run in the terminal.
It should support two players or one player against a computer opponent.

**Requirements**
|id|requirement|how verified|
|---|---|---|
|r1|x always plays first|test that the first mark placed is x|
|r2|game detects a win (row, col, diag) and draw| test for all win directions and full board|
|r3|game has a two player and one player vs computer mode|manual test of all modes|
|r4|board is printed after every move|test that board is printed after each move|
|r5|a move is a row and column numbered from 1. Moves that don't satisfy this are rejected and don't consume a turn|tests for taken, off board and bad input|
|r6|in vs computer mode, human goes first|test that player move is first in vs computer mode|

\
**Components**
|File|Purpose|
|---|---|
|board.py|the board class|
|ai.py|the ai classes|
|game.py|turns, modes and win/lose checks|
|main.py|menus, prompt and printing|
|tests/|pytest tests|
|PLAN.md|the plan|
|README.md|how to run and testing|
|/ci.yml|ci pipeline|

\
**Decisions**
