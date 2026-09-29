def check_sudoku(sudoku):
    for i in range(9):
        numbers = []

        # Check row
        for j in range(9):
            number = sudoku[i][j]

            if number != 0:
                if number in numbers:
                    return False

                numbers.append(number)

        # Check column
        numbers = []

        for j in range(9):
            number = sudoku[j][i]

            if number != 0:
                if number in numbers:
                    return False

                numbers.append(number)

    # Check 3x3 boxes
    for row in range(0, 9, 3):
        for column in range(0, 9, 3):
            numbers = []

            for i in range(row, row + 3):
                for j in range(column, column + 3):
                    number = sudoku[i][j]

                    if number != 0:
                        if number in numbers:
                            return False

                        numbers.append(number)

    return True
