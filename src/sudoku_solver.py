from src.sudoku import Sudoku

class Sudoku_Solver():
    """
    Solves a Sudoku board using the backtracking algorithm

    Class Invariants:
    - sudoku is a Sudoku object
    - sudoku is never null

    Methods:
        - solve: Solves the Sudoku board using the backtracking algorithm
    """
    def __init__(self, sudoku):
        self.__sudoku = sudoku

    @property
    def sudoku(self):
        return self.__sudoku

    def _find_empty_cell(self):
        for i in range(9):
            for j in range(9):
                if self.sudoku.is_empty(i, j):
                    return i, j
        return None

    def solve(self):
        """
        Solves the Sudoku board using the backtracking algorithm
        :return: boolean
        """

        # If there is no unassigned
        # location, we are done
        if self._find_empty_cell() is None:
            return True

        # get the next empty cell
        row, col = self._find_empty_cell()

        # loop through 1 to 9
        for num in range(1, 10):

            # test if the number is valid
            if self.sudoku.is_valid(row, col, num):

                # print(self.sudoku)
                # print("writing to {} {} the number {}\n".format(row, col, num))
                # test a number
                self.sudoku.write(row, col, num)

                # return true if valid
                if self.solve():
                    return True

                # if false, backtrack to previous cell
                # print("backtracking from {} {}\n".format(row, col))
                self.sudoku.write(row, col, None)
        return False

    def __str__(self):
        return str(self.sudoku)
