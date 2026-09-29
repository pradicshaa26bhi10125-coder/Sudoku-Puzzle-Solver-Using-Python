def get_sudoku():
    sudoku = []

    print("Enter 9 rows.")
    print("Use 0 for empty spaces.")

    for i in range(9):
        row = []

        for j in range(9):
            number = int(input("Enter number: "))
            row.append(number)

        sudoku.append(row)

    return sudoku
