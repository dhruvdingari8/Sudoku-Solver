import unittest
from sudoku import Sudoku
from sudoku_solver import Sudoku_Solver


class MyTestCase(unittest.TestCase):

    def setUp(self):
        # Create a board for testing
        board1 = [[None, None, None, None, None, 5, None, None, 4],
                 [None, None, 7, None, None, None, 8, None, None],
                 [None, 8, None, None, None, 1, None, 3, None],
                 [None, None, None, 9, None, None, None, 7, None],
                 [None, None, None, None, None, None, None, None, None],
                 [None, 3, None, None, None, 6, None, None, None],
                 [None, 5, None, 3, None, None, None, 6, None],
                 [None, None, 4, None, None, None, 5, None, None],
                 [1, None, None, 8, None, None, None, None, None]]
        self.solboard1 = [[2, 1, 3, 6, 8, 5, 7, 9, 4],
                          [4, 6, 7, 2, 3, 9, 8, 1, 5],
                          [5, 8, 9, 4, 7, 1, 2, 3, 6],
                          [6, 2, 5, 9, 1, 3, 4, 7, 8],
                          [9, 4, 1, 7, 2, 8, 6, 5, 3],
                          [7, 3, 8, 5, 4, 6, 9, 2, 1],
                          [8, 5, 2, 3, 9, 4, 1, 6, 7],
                          [3, 7, 4, 1, 6, 2, 5, 8, 9],
                          [1, 9, 6, 8, 5, 7, 3, 4, 2]]
        self.sudoku1 = Sudoku(board1)
        self.solver1 = Sudoku_Solver(self.sudoku1)
        # Test the solve method of Sudoku_Solver
        board2 = [[5, None, None, None, None, 5, None, None, 4],
                 [None, None, 7, None, None, None, 8, None, None],
                 [None, 8, None, None, None, 1, None, 3, None],
                 [None, None, None, 9, None, None, None, 7, None],
                 [None, None, None, None, None, None, None, None, None],
                 [None, 3, None, None, None, 6, None, None, None],
                 [None, 5, None, 3, None, None, None, 6, None],
                 [None, None, 4, None, None, None, 5, None, None],
                 [None, None, None, 8, None, None, None, None, 1]]
        self.sudoku2 = Sudoku(board2)
        self.solver2 = Sudoku_Solver(self.sudoku2)

    def test_solve(self):
        # Test the solve method of Sudoku_Solver
        self.assertTrue(self.solver1.solve())
        # loop through the board and check if all cells are equal to the correct cell in the solution board above
        print(self.sudoku1)
        print(Sudoku(self.solboard1))
        for i in range(9):
            for j in range(9):
                print("At row: " + str(i) + " and col: " + str(j))
                self.assertEqual(self.sudoku1.board[i][j], self.solboard1[i][j])

        print(self.solver2.solve())



if __name__ == '__main__':
    unittest.main()
