# AI-Assignment2

I have used Python programming language for working on this assignment.

### How to compile and execute

I have written two Python programs. One is basic sudoku solver that uses naive backtracking algorithm where the selection of variables and assignment of values can be done in order. The other sudoku solver that uses smart backtracking algorithm that is a combination of minimum remaining values (MRV), least constraining value (LCV), and forward checking while implementing the backtracking algorithm. Both the programs considers the input puzzle and parses the sudoku data file.

I have considered the sample inputs from the link: [http://www.websodoku.com](http://www.websodoku.com). I have considered easy, medium, hard and evil puzzles two each and saved all the puzzles in text file with the name sampleinputs.txt. The Python progeam considers the input from the sudokuinput.txt file. The puzzle has to be updated in this file each time to try different puzzles. 

**one new line** should be provided after the input puzzle so that the program understands that complete input is considered.

### Naive Backtracking Algorithm
The Naive backtracking method is implemented by traversing through each empty space in the sudoku puzzle and checking for the valid values (for numbers between 1 and 9). Wrote a function to check the validity of values row-wise and column-wise, if the particular value can not be placed because of the other constraints then the program backtracks to the previous position where another value was already checked for validity. This program traverses row-by-row in search of empty spaces on sudoku puzzle. This takes a lot of branching hence is the name naive method.

### Smart Backtracking Algorithm


