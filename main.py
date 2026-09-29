from app.display import display_sudoku
from app.checker import check_sudoku
from app.solver import solve_sudoku
from app.input_handler import get_sudoku


print("SUDOKU CHECKER AND SOLVER")
print("-------------------------")

sudoku = get_sudoku()

print("\nGiven Sudoku:")
display_sudoku(sudoku)

if check_sudoku(sudoku):
    print("\nSudoku is valid.")

    if solve_sudoku(sudoku):
        print("\nSolved Sudoku:")
        display_sudoku(sudoku)
    else:
        print("\nThis Sudoku cannot be solved.")
else:
    print("\nSudoku is invalid.")
