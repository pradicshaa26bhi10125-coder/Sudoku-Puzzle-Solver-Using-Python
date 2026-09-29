# 🧩 Sudoku Puzzle Solver Using Python

![Python Version](https://img.shields.io/badge/python-3.x-blue.svg)

A clean, interactive command-line application written in Python that validates and solves standard **9x9 Sudoku puzzles** using a **backtracking algorithm**.

---

## 📌 Features

- **Input Validation:** Automatically checks rows, columns, and $3 \times 3$ sub-grids to confirm the board is valid before solving.
- **Backtracking Solver:** Uses standard depth-first search / backtracking to find the solution.
- **Interactive CLI:** Prompts user input for grid numbers directly in the terminal interface.
- **Zero External Dependencies:** Built completely with standard Python libraries.

---

## 🛠️ Prerequisites

Ensure you have the following installed on your system:

* **Python 3.x**: [Download Python](https://www.python.org/downloads/)
* **Git**: [Download Git](https://git-scm.com/downloads)
* **pip** (Standard Python Package Installer, pre-packaged with Python)

---

## 📥 Installation & Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/pradicshaa26bhi10125-coder/Sudoku-Puzzle-Solver-Using-Python.git
   ```

2. **Navigate to the project directory:**
   ```bash
   cd Sudoku-Puzzle-Solver-Using-Python
   ```

3. **(Optional) Verify Python and Pip installation:**
   ```bash
   python --version
   pip --version
   ```

---

## 🚀 Usage

Run the Python script directly from your terminal:

```bash
python "pradicshaa 26bhi10125.py"
```

> **Note:** You may rename the script to `main.py` or `sudoku_solver.py` for convenience:
> ```bash
> python main.py
> ```

### Input Instructions:
1. Enter each number for the 9x9 board row by row when prompted.
2. Use `0` to denote empty spaces.
3. The program will validate the initial state and output the solved grid if a valid solution exists.

---

## 🧠 How It Works

1. **Validation (`check_sudoku`):** Checks every row, column, and $3 \times 3$ box to ensure no duplicate numbers (1–9) exist in the non-empty cells.
2. **Solving (`solve_sudoku`):** 
   - Finds an unassigned spot (`0`).
   - Recursively tries digits from `1` to `9`.
   - If a valid placement leads to a solution, it returns `True`.
   - If none work, it backtracks (`sudoku[row][column] = 0`) and attempts the next possibility.

---

## 👤 Author

* **Repository:** [Sudoku-Puzzle-Solver-Using-Python](https://github.com/pradicshaa26bhi10125-coder/Sudoku-Puzzle-Solver-Using-Python)
* **GitHub Profile:** [@pradicshaa26bhi10125-coder](https://github.com/pradicshaa26bhi10125-coder)
