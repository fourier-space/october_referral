"""
question1.py - programming logic and unit tests

Wordle is a game, where players attempt to guess a hidden five letter word.
https://en.wikipedia.org/wiki/Wordle

You are going to implement the wordle clue function.

The function takes two five letter strings,
the solution and the guess,
and will return the corresponding clue.

The clue will be a string of five characters from
"g", "y", and "."
for green, yellow, and blank.

A clue letter is green if the guess and solution in the corresponding position match.
A clue letter is yellow if the guess letter in that position is somewhere else in the solution
Otherwise the clue is blank.

The exact specification, that includes what to do in the case of repeated letters
is given in the unit test file.

Examples,
solution: "REBUS"
   guess: "PLANK"
 => clue: "....."

solution: "REBUS"
   guess: "ARISE"
 => clue: ".y.yy"

solution: "REBUS"
   guess: "ROUTE"
 => clue: "g.y.y"

solution: "REBUS"
   guess: "RULES"
 => clue: "gy.yg"

solution: "REBUS"
   guess: "REBUS"
 => clue: "ggggg"

TOTAL POINTS AVAILABLE: 5 

Code Functionality (5)
5 points - All unit tests pass and including unseen examples.
1-4 points - 1 point per passing unit test.
0 - No unit tests pass

"""

GREEN = "g"
YELLOW = "y"
NONE = "."

def wordle(solution, guess):
    clue = ""
    return clue
