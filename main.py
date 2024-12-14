from src.sudoku import Sudoku
from src.sudoku_solver import Sudoku_Solver


# main function
def main():


    while True:
        boardstr = input("Enter the board as a string of 81 numbers, 0 for empty cells: ")
        if not all(c in '0123456789' for c in boardstr):
            print("Invalid input. Please enter only numbers.")
        elif len(boardstr) != 81:
            print("Invalid input. Please enter 81 numbers.")
        else:
            break

    # initialize a 2d 9x9 list
    board = [[None for _ in range(9)] for _ in range(9)]
    # fill the board with the given numbers, converting 0 to None
    for i in range(9):
        for j in range(9):
            board[i][j] = int(boardstr[i * 9 + j])
            if board[i][j] == 0:
                board[i][j] = None

    s = Sudoku(board)
    print("The following board was entered:")
    print(s)

    print("Solving\n.\n.\n.\n\n\n")
    solver = Sudoku_Solver(s)
    if solver.solve() is True:
        print(s)
    else:
        print("No solution found.")



if __name__ == '__main__':
    main()

