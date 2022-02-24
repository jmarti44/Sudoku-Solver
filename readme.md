### Instructions for running
1. The `Sudoku_Solver.py` file can be compiled with the following terminal instruction command with the given arguments for the user to choose which algorithm to run
2. ```python3 Sudoku_solver.py --algorithm ac3``` to run the arc consistency algorithm and ```python3 Sudoku_solver.py --algorithm backtracking``` to run the backtracking algorithm and
   ```python3 Sudoku_solver.py --algorithm both``` to run both algorithms, in cases where the arc consistency algorithm is not the optimal solution 
3. The user will be shown a series of grids to choose from to run the sudoku solver based on the given terminal arguments. It is recommended to expand the terminal window to see the entire output. The grids shown are taken from the sample test cases given to us.
4. The program currently will only run with the following options: `Grid 1`, `Grid 2`, `Grid 3`, `Grid 4`, `Grid 5`. `Grid 6`
5. 
   
**The program requires the user to compile the program between different test runs**



### Dependencies
Certain Libraries will need to be installed. A note worthy library to install is `sortedcontainers`.


### Files
```Homework I.pdf``` contains the worked out solutions for the homework

```ac3.py``` contains the arc consistency algorithm implementation


```foward_checking.py``` contains the backtracking + foward checking algorithm implementation.

```Utility.py``` contains a series of helper functions, which include the CSP Class, and the Sudoku class.



### References
The implementation of the CSP class and the associated backtracking and arc consistency helper functions was based on the following github repository.
https://github.com/aimacode/aima-python/blob/master/csp.py








