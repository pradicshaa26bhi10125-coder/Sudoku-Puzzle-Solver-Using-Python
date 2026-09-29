# 5.2 Project Statement: Sudoku Puzzle Solver

## 1. Problem Statement
Sudoku is a popular logic-based number-placement puzzle that requires players to fill a $9 \times 9$ grid such that each row, column, and $3 \times 3$ sub-grid contains all digits from $1$ to $9$ without repetition. 

Manually solving complex Sudoku puzzles can be extremely time-consuming, and human error often leads to invalid board states late in the solving process. Additionally, verifying whether a given puzzle configuration is valid or solvable is difficult without systematically exploring all potential number combinations. There is a need for a lightweight, fast, and automated programmatic tool that can validate user-provided board setups and deterministically compute solutions using optimal search algorithms.

---

## 2. Scope of the Project

### In-Scope
* **Standard Grid Support:** Processing standard $9 \times 9$ Sudoku puzzle configurations.
* **Input Validation:** Checking rows, columns, and $3 \times 3$ sub-grids to ensure the starting puzzle obeys standard Sudoku rules before solving.
* **Algorithmic Solving:** Employing a recursive backtracking algorithm (depth-first search) to systematically find grid solutions.
* **Command-Line Interface (CLI):** Interactive terminal prompts allowing users to manually enter puzzle values row-by-row (using `0` for empty cells).
* **Solvability Feedback:** Clear notification regarding board validity and whether a solution exists.

### Out-of-Scope
* Graphical User Interface (GUI) or web-based frontend applications.
* Computer vision / OCR capabilities to scan puzzle images from photos or camera feeds.
* Automatic generation of new Sudoku puzzles or difficulty level classifications.
* Support for non-standard board sizes (e.g., $4 \times 4$, $6 \times 6$, or $16 \times 16$).

---

## 3. Target Users

1. **Puzzle Enthusiasts:** Players seeking a quick tool to check their manual progress or obtain answers to particularly difficult puzzles.
2. **Students & Computer Science Learners:** Individuals studying foundational programming concepts, such as recursion, depth-first search (DFS), matrix traversal, and backtracking algorithm implementations in Python.
3. **Educators & Tutors:** Instructors looking for a clean, dependency-free reference implementation of grid-based search problems to demonstrate in classroom settings.

---

## 4. High-Level Features

* **Automated Board Validation:** Evaluates the initial matrix state prior to execution to detect duplicate numbers in any row, column, or $3 \times 3$ sub-grid.
* **Backtracking Solver Engine:** Efficiently traverses the state space to fill empty cells ($0$), automatically backtracking when an invalid state is encountered until a full solution is reached.
* **Interactive Command-Line Interface:** Prompts the user step-by-step for grid entries and presents both the initial input and completed solution in a formatted $9 \times 9$ view.
* **Zero-Dependency Architecture:** Built strictly using native Python data structures, eliminating external package dependencies for maximum portability across operating systems.