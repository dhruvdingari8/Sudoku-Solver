import unittest
from src.sudoku import Sudoku


class MyTestCase(unittest.TestCase):
    s1 = None

    def setUp(self):
        board = [
            [None, None, None, None, None, 5, None, None, 4],
            [None, None, 7, None, None, None, 8, None, None],
            [None, 8, None, None, None, 1, None, 3, None],
            [None, None, None, 9, None, None, None, 7, None],
            [None, None, None, None, None, None, None, None, None],
            [None, 3, None, None, None, 6, None, None, None],
            [None, 5, None, 3, None, None, None, 6, None],
            [None, None, 4, None, None, None, 5, None, None],
            [1, None, None, 8, None, None, None, None, None]
        ]
        self.s1 = Sudoku(board)

    def test_subgrid(self):
        # Tests the _subgrid method of Sudoku
        self.assertEqual(self.s1._subgrid(0, 0), (0, 0))
        self.assertEqual(self.s1._subgrid(0, 1), (0, 0))
        self.assertEqual(self.s1._subgrid(0, 3), (0, 1))
        self.assertEqual(self.s1._subgrid(0, 4), (0, 1))
        self.assertEqual(self.s1._subgrid(0, 7), (0, 2))
        self.assertEqual(self.s1._subgrid(0, 8), (0, 2))
        self.assertEqual(self.s1._subgrid(1, 2), (0, 0))
        self.assertEqual(self.s1._subgrid(1, 5), (0, 1))
        self.assertEqual(self.s1._subgrid(1, 8), (0, 2))
        self.assertEqual(self.s1._subgrid(2, 0), (0, 0))
        self.assertEqual(self.s1._subgrid(2, 4), (0, 1))
        self.assertEqual(self.s1._subgrid(2, 8), (0, 2))
        self.assertEqual(self.s1._subgrid(3, 0), (1, 0))
        self.assertEqual(self.s1._subgrid(3, 4), (1, 1))
        self.assertEqual(self.s1._subgrid(3, 8), (1, 2))
        self.assertEqual(self.s1._subgrid(4, 0), (1, 0))
        self.assertEqual(self.s1._subgrid(4, 4), (1, 1))
        self.assertEqual(self.s1._subgrid(6, 8), (2, 2))
        self.assertEqual(self.s1._subgrid(8, 8), (2, 2))

    def test_in_starting_board(self):
        # Tests the _in_starting_board method of Sudoku
        self.assertFalse(self.s1._in_starting_board(0, 0))
        self.assertFalse(self.s1._in_starting_board(0, 1))
        self.assertFalse(self.s1._in_starting_board(0, 2))
        self.assertFalse(self.s1._in_starting_board(0, 3))
        self.assertFalse(self.s1._in_starting_board(0, 4))
        self.assertTrue(self.s1._in_starting_board(0, 5))
        self.assertFalse(self.s1._in_starting_board(0, 6))
        self.assertFalse(self.s1._in_starting_board(0, 7))
        self.assertTrue(self.s1._in_starting_board(0, 8))
        self.assertFalse(self.s1._in_starting_board(1, 0))
        self.assertFalse(self.s1._in_starting_board(1, 1))
        self.assertTrue(self.s1._in_starting_board(1, 2))
        self.assertFalse(self.s1._in_starting_board(1, 3))
        self.assertFalse(self.s1._in_starting_board(1, 4))
        self.assertFalse(self.s1._in_starting_board(1, 5))
        self.assertTrue(self.s1._in_starting_board(1, 6))
        self.assertFalse(self.s1._in_starting_board(1, 7))
        self.assertFalse(self.s1._in_starting_board(1, 8))
        self.assertFalse(self.s1._in_starting_board(2, 0))
        self.assertTrue(self.s1._in_starting_board(2, 1))
        self.assertFalse(self.s1._in_starting_board(2, 2))
        self.assertFalse(self.s1._in_starting_board(2, 3))
        self.assertFalse(self.s1._in_starting_board(2, 4))
        self.assertTrue(self.s1._in_starting_board(2, 5))
        self.assertFalse(self.s1._in_starting_board(2, 6))
        self.assertTrue(self.s1._in_starting_board(2, 7))
        self.assertFalse(self.s1._in_starting_board(2, 8))

    def test_is_empty(self):
        # Tests the is_empty method of Sudoku
        self.assertTrue(self.s1.is_empty(0, 0))
        self.assertTrue(self.s1.is_empty(0, 1))
        self.assertFalse(self.s1.is_empty(0, 5))

if __name__ == '__main__':
    unittest.main()
