from src.sudoku import Sudoku

class Sudoku_Solver():
    def __init__(self, sudoku):
        self.__sudoku = sudoku

    @property
    def sudoku(self):
        return self.__sudoku

    def find_empty_cell(self):
        for i in range(9):
            for j in range(9):
                if self.sudoku.is_empty(i, j):
                    return i, j
        return None

    def solve(self):

        # 'l' is a list variable that keeps the
        # record of row and col in
        # find_empty_location Function
        l = self.find_empty_cell()

        # If there is no unassigned
        # location, we are done
        if self.find_empty_cell() is None:
            return True

        # Assigning list values to row and col
        # that we got from the above Function
        row = l[0]
        col = l[1]

        # consider digits 1 to 9
        for num in range(1, 10):

            # if looks promising
            if self.sudoku._is_valid(row, col, num):

                print(self.sudoku)
                print("writing to {} {} the number {}\n".format(row, col, num))
                # make tentative assignment
                self.sudoku.write(row, col, num)

                # return, if success,
                # ya !
                if self.solve():
                    return True

                # failure, unmake & try again
                print("backtracking from {} {}\n".format(row, col))
                self.sudoku.write(row, col, None)

        # this triggers backtracking
        return False

    def __str__(self):
        return str(self.sudoku)
