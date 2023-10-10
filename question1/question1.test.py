"""
question1.test.py

Unit tests for question1.py.
"""

import unittest
from question1 import wordle

class TestQuestion1(unittest.TestCase):
    def test_match_green(self):
        """
        Letters in the same position in the guess and solution
        that match
        are green in the clue.
        """

        self.assertEqual(
            wordle( # Guess and solution the same – all green.
                "SCOPE",
                "SCOPE"
            ),  "ggggg"
        )

        self.assertEqual(
            wordle("SCOPE", "GRATE")[4], # Last letter [4] matches, should be green.
            "g"
        )

    def test_not_match_not_green(self):
        """
        Letters in the same position in the guess and solution
        that do not match
        are not green in the clue.
        """

        self.assertEqual(
            wordle(
                "SCOPE",
                "BLIND"
            ),  "....."
        )

        self.assertNotEqual(
            wordle("CRUSH", "PANIC")[0], # letter [0] clue is yellow not green.
            "g"
        )

        self.assertNotEqual(
            wordle("ADULT", "GLORY")[1], # letter [1] clue is blank not green.
            "g"
        )

    def test_yellow(self):
        """
        Letters in the guess that aren't clued green
        that can be matched to a letter in the solution in any position
        that isn't itself clued green
        and hasn't been matched by a previous guess letter
        are yellow in the clue
        """

        self.assertEqual(
            wordle(
                "SCOPE",
                "COPES"
            ),  "yyyyy"
        )

        self.assertEqual(
            wordle(
                "TROVE",
                "SMELT"
            ),  "..y.y"
        )

        self.assertEqual(
            wordle(
                "VAPID",
                "ANTIC"
            ),  "y..g."
        )

    def test_mutliple_letters(self):
        """
        Edge cases with repeated letters.
        Testing properties above.
        """

        self.assertEqual(
            wordle(
                "CANOE",
                "NATAL"
            ),  "yg..."
        )

        self.assertEqual(
            wordle(
                "NATAL",
                "CANOE"
            ),  ".gy.."
        )

        self.assertEqual(
            wordle(
                "SCOPE",
                "GEESE"
            ),  "...yg"
        )

        self.assertEqual(
            wordle(
                "COPES",
                "GEESE"
            ),  ".y.y."
        )

if __name__ == '__main__':
    unittest.main()
