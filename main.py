from src.sudoku import Sudoku
from src.sudoku_solver import Sudoku_Solver

# main function
def main():
    # Generate a Sudoku board as a 9x9 square 2D list, where empty cells are represented by None
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

    # Create a Sudoku object
    sudoku = Sudoku(board)
    print(sudoku)

    # Solve the Sudoku board
    ss = Sudoku_Solver(sudoku)
    ss.solve()
    print(ss)



if __name__ == '__main__':
    main()