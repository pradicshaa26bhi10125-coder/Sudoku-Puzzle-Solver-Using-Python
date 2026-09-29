from app.checker import check_sudoku


def solve_sudoku(sudoku):
    for row in range(9):
        for column in range(9):

            if sudoku[row][column] == 0:

                for number in range(1, 10):
                    sudoku[row][column] = number

                    if check_sudoku(sudoku):
                        if solve_sudoku(sudoku):
                            return True

                sudoku[row][column] = 0

                return False

    return True
