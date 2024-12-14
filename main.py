from src.sudoku import Sudoku
from src.sudoku_solver import Sudoku_Solver


# main function
def main():
    # ask the user for the board numbers, where 0 represents an empty cell
    boardstr = input("Enter the board numbers (0 for empty cells): ")
    # initialize a 2d 9x9 list
    board = [[None for _ in range(9)] for _ in range(9)]
    # fill the board with the given numbers, converting 0 to None
    for i in range(9):
        for j in range(9):
            board[i][j] = int(boardstr[i * 9 + j])
            if board[i][j] == 0:
                board[i][j] = None


    print(board)

    s = Sudoku(board)
    solver = Sudoku_Solver(s)
    solver.solve()
    print(s)



if __name__ == '__main__':
    main()

