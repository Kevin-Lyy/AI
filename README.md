# AI
# Word ladder
# Sudoku
In the sudoku folder are, the testing boards, a naive sudoku solver and a smart sudoku solver. 
The naive solver goes one by one and tries fill out the board with a number it checks to fit. It checks the row, the column and the 
3 by 3 box, if it runs into a box that cannot work with any number it goes back one stop to the last spot it fills and tries again.
The smart solver also goes through the board one by one but before guessing it does a scan and fills out pieces of the board that 
are guaranteed then it starts the guess process and rescans until the board is filled 
