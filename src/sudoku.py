class Sudoku:
    """
    Sudoku class that represents a Sudoku board

    Class Invariants:
        - board is a 9x9 2D square list
        - board is never null
        - board can only be set when creating a new Sudoku object
        - an empty cell is represented by None
        - a valid Sudoku board has no duplicate numbers in each row, column, and 3x3 subgrid
        - numbers in the starting board cannot be changed

    Has attributes:
        - board: a 2D list representing the Sudoku board
        - starting_board: a 2D list representing the starting Sudoku board (cannot be changed)

    Has methods:
        - __str__: returns a string representation of the Sudoku board
        - is_empty(row, col): returns True if the cell at the given row and column is empty, False otherwise
        - _is_valid: returns True if the Sudoku board is valid, False otherwise
        - write(row, col): writes a number to the cell at the given row and column
        - num_at(row, col): returns the number at the cell at the given row and column
    """

    @property
    def board(self):
        return self.__board

    @property
    def starting_board(self):
        return self.__starting_board

    def __init__(self, board):
        self.__board = board
        self.__starting_board = [[cell for cell in row] for row in board]




    def is_empty(self, row, col):
        """
        Returns True if the cell at the given row and column is empty, False otherwise
        """
        return self.board[row][col] is None

    def _is_valid(self, row, col, num):
        """
        Returns true if the Sudoku board is valid, False otherwise
        Valid is defined by each row and column containing no duplicate numbers
        :return: Boolean defining validity of board
        """

        # Check if the row contains the number.
        if self._does_row_contain(row, num):
            # Return False if the row contains the number.
            return False
        # Check if the column contains the number.
        if self._does_col_contain(col, num):
            # Return False if the column contains the number.
            return False
        # Check if the subgrid contains the number.
        if self._does_subgrid_contain(row, col, num):
            # Return False if the subgrid contains the number.
            return False

        # If all checks pass, return True.
        return True

    def _does_row_contain(self, row, num):
        """
        Returns True if the given row contains the given number, False otherwise
        :return: Boolean
        """

        # Iterate through the row.
        for i in range(9):
            # Check if the number is in the row.
            if self.board[row][i] == num:
                # Return True if the number is in the row.
                print("row contains number" + str(num))
                return True

        print("row does not contain number" + str(num))
        # Return False if the number is not in the row.
        return False

    def _does_col_contain(self, col, num):
        """
        Returns True if the given column contains the given number, False otherwise
        :return: Boolean
        """

        # Iterate through the column.
        for i in range(9):
            # Check if the number is in the column.
            if self.board[i][col] == num:
                # Return True if the number is in the column.
                print("col contains number" + str(num))
                return True

        print("col does not contain number" + str(num))
        # Return False if the number is not in the column.
        return False

    def _does_subgrid_contain(self, row, col, num):
        """
        Returns True if the 3x3 subgrid that the cell at the given row and column is in contains the given number, False otherwise
        :return: Boolean
        """

        # Get the row and column of the top left cell of the subgrid.
        start_row, start_col = self._subgrid(row, col)

        # Iterate through the subgrid.
        for i in range(start_row*3, start_row*3 + 3):
            for j in range(start_col*3, start_col*3 + 3):
                # Check if the number is in the subgrid.
                if self.board[i][j] == num:
                    # Return True if the number is in the subgrid.
                    print("subgrid contains number" + str(num))
                    return True


        print("subgrid does not contain number" + str(num))
        # Return False if the number is not in the subgrid.
        return False




    def write(self, row, col, num):
        """
        Writes a number to the cell at the given row and column

        :param row: int
        :param col: int
        :param num: int
        :raise ValueError: if the cell at the given row and column is not empty
        :raise ValueError: if the number is not between 1 and 9
        :raise ValueError: if the number is already in the same row, column, or 3x3 subgrid
        """

        # Check if the cell is a starting value
        if self._in_starting_board(row, col):
            # Raise an error if the cell is a starting value
            raise ValueError('Cannot change starting value')
        else:
            if (num == None):
                self.board[row][col] = None
                return
            else:
                # Raise an error if the number is not between 1 and 9
                if num not in range(1, 10):
                    raise ValueError('Number must be between 1 and 9')
                # Raise an error if the number is already in the same row, column, or 3x3 subgrid
                if not self._is_valid(row, col, num):
                    raise ValueError('Number already in row, column, or subgrid')

            # Write the number to the cell
            self.board[row][col] = num


    def _in_starting_board(self, row, col):
        """
        Returns True if the cell at the given row and column is not in the starting board, False otherwise
        :return: Boolean
        """
        return (self.starting_board[row][col] != None)

    def _subgrid(self, row, col):
        """
        Returns the 3x3 subgrid that the cell at the given row and column is in

        :return: Coords of subgrid as Tuple
        """

        # Calculate the row and column of the top left cell of the subgrid.
        start_row = row - row % 3
        start_col = col - col % 3

        # Return the row and column of the top left cell of the subgrid.
        return int(start_row/3), int(start_col/3)

    def num_at(self, row, col):
        """
        Returns the number at the cell at the given row and column
        """
        return self.board[row][col]

    def __str__(self):
        """
        Returns a string representation of the Sudoku board with empty cells represented by '.'
        """
        result = ""

        # Iterate through the rows of the board
        # for every 3 rows, add a horizontal line
        # for every 3 cols, add a vertical line
        # replace None with '.'
        # no recursion

        for i in range(9):
            if i % 3 == 0 and i != 0:
                result += "------+-------+------\n"
            for j in range(9):
                if j % 3 == 0 and j != 0:
                    result += "| "
                if self.board[i][j] is None:
                    result += ". "
                else:
                    result += str(self.num_at(i, j)) + " "
            result += "\n"

        return result