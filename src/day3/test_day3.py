import os
from unittest import TestCase

from day3.day3 import read_input, solve_1, solve_2

_MOCK_INPUT_FILEPATH = os.path.join(os.path.dirname(__file__), "mock_input.txt")


class TestDay3(TestCase):
    def test_should_solve_1(self):
        rows = read_input(input_filepath=_MOCK_INPUT_FILEPATH)
        result = solve_1(rows)
        self.assertEqual(result, 7)

    def test_should_solve_2(self):
        """
        Right 1, down 1.
        Right 3, down 1. (This is the slope you already checked.)
        Right 5, down 1.
        Right 7, down 1.
        Right 1, down 2.
        """
        rows = read_input(input_filepath=_MOCK_INPUT_FILEPATH)
        res1 = solve_2(rows=rows, right=1, down=1)
        res2 = solve_2(rows=rows, right=3, down=1)
        res3 = solve_2(rows=rows, right=5, down=1)
        res4 = solve_2(rows=rows, right=7, down=1)
        res5 = solve_2(rows=rows, right=1, down=2)

        self.assertEqual(res1, 2)
        self.assertEqual(res2, 7)
        self.assertEqual(res3, 3)
        self.assertEqual(res4, 4)
        self.assertEqual(res5, 2)
        self.assertEqual(res1 * res2 * res3 * res4 * res5, 336)
