# AI-Assignment3

I have used Python programming language for working on this assignment.

### How to compile and execute

I have written two Python programs. One is basic sudoku solver that uses naive backtracking algorithm where the selection of variables and assignment of values can be done in order. The other sudoku solver that uses smart backtracking algorithm that is a combination of minimum remaining values (MRV), forward checking and also the naive backtracking while implementing the backtracking algorithm. Both the programs considers the input puzzle and parses the sudoku data file.

I have considered the sample inputs from the link: [http://www.websodoku.com](http://www.websodoku.com). I have considered easy, medium, hard and evil puzzles two each and saved all the puzzles in text file with the name sampleinputs.txt. The Python progeam considers the input from the sudokuinput.txt file. The puzzle has to be updated in this file each time to try different puzzles. 

            python <python_filename>
            
In this case there are 2 filenames:

a. For Naive backtracking algorithm: filename will be naivebacktrackingsolver.py

b. For smart backtracking algorithm: filename will be smartbacktrackingsolver.py

**one new line** should be provided after the input puzzle so that the program understands that complete input is considered.

After execution the output of all the puzzles is saved in output.txt file
