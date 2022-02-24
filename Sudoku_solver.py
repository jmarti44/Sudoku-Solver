

# from Utility import convertToString

from hashlib import new
from re import A, S
from Utility import *
import argparse



from Utility import Sudoku
from ac3 import*
from foward_checking import *




parser = argparse.ArgumentParser()
parser.add_argument("--algorithm")
args = parser.parse_args()



matrix_1 = [[5, 3, 4, 6, 7, 8, 9, 0, 0], 
            [6, 7, 2, 1, 9, 5, 3, 4, 8], 
            [1, 9, 8, 3, 4, 2, 5, 6, 7], 
            [8, 5, 9, 7, 6, 1, 4, 2, 3], 
            [4, 2, 6, 8, 5, 3, 7, 9, 1], 
            [7, 1, 3, 9, 2, 4, 8, 5, 6], 
            [9, 6, 1, 5, 3, 7, 2, 8, 4], 
            [2, 8, 7, 4, 1, 9, 6, 3, 5], 
            [3, 4, 5, 2, 8, 6, 1, 7, 9]]


matrix_2 = [[6, 5, 0, 7, 3, 0, 0, 8, 0], 
            [0, 0, 0, 4, 8, 0, 5, 3, 0], 
            [8, 4, 0, 9, 2, 5, 0, 0, 0], 
            [0, 9, 0, 8, 0, 0, 0, 0, 0], 
            [5, 3, 0, 2, 0, 9, 6, 0, 0], 
            [0, 0, 6, 0, 0, 0, 8, 0, 0], 
            [0, 0, 9, 0, 0, 0, 0, 0, 6], 
            [0, 0, 7, 0, 0, 0, 0, 5, 0], 
            [1, 6, 5, 3, 9, 0, 4, 7, 0]]




matrix_3 = [[0, 5, 0, 0, 7, 0, 0, 0, 1], 
            [8, 7, 6, 0, 2, 1, 9, 0, 3], 
            [0, 0, 0, 0, 3, 5, 0, 0, 0], 
            [0, 0, 0, 0, 4, 3, 6, 1, 0], 
            [0, 4, 0, 0, 0, 9, 0, 0, 2], 
            [0, 1, 2, 0, 5, 0, 0, 0, 4], 
            [0, 8, 9, 0, 6, 4, 0, 0, 0], 
            [0, 0, 0, 0, 0, 7, 0, 0, 0], 
            [1, 6, 7, 0, 0, 2, 5, 4, 0]]


matrix_4 = [[0, 0, 0, 9, 3, 8, 0, 4, 0], 
            [0, 0, 0, 7, 6, 0, 0, 0, 2], 
            [7, 4, 0, 5, 0, 0, 0, 8, 0], 
            [8, 0, 0, 6, 7, 5, 0, 1, 3], 
            [0, 7, 0, 3, 0, 2, 8, 0, 0], 
            [3, 2, 0, 0, 4, 0, 0, 0, 0], 
            [0, 0, 0, 0, 5, 6, 3, 2, 0], 
            [0, 5, 0, 4, 0, 0, 0, 0, 0], 
            [1, 0, 6, 2, 0, 0, 0, 5, 0]]



matrix_5 =[[0, 8, 0, 0, 0, 0, 0, 0, 1], 
            [0, 0, 4, 3, 0, 0, 9, 8, 0], 
            [3, 0, 1, 0, 0, 8, 7, 0, 0], 
            [0, 1, 0, 5, 4, 0, 0, 6, 0], 
            [0, 0, 0, 2, 9, 0, 4, 1, 0], 
            [0, 4, 3, 0, 0, 6, 0, 9, 0], 
            [0, 0, 8, 0, 0, 5, 0, 3, 0], 
            [0, 6, 7, 0, 3, 9, 5, 0, 8], 
            [1, 0, 5, 0, 8, 0, 0, 0, 0]]



matrix_6= [[8, 7, 0, 0, 0, 0, 6, 5, 2], 
            [0, 0, 0, 0, 7, 2, 4, 0, 0], 
            [0, 3, 2, 0, 5, 0, 0, 0, 0], 
            [0, 0, 8, 0, 0, 5, 3, 0, 4], 
            [6, 0, 0, 9, 0, 3, 0, 0, 0], 
            [0, 1, 3, 7, 0, 0, 0, 0, 0], 
            [5, 0, 9, 4, 0, 7, 0, 0, 0], 
            [3, 0, 0, 1, 0, 9, 0, 7, 0], 
            [1, 2, 0, 0, 0, 6, 0, 4, 9]]



###Outputing Menu Grids
print('Grid 1\n')
inputString = convertToString(matrix_1)
newSudoku = Sudoku(inputString)
newSudoku.display(newSudoku.infer_assignment())
print('------------------------------\n')
print("Grid 2\n")
inputString = convertToString(matrix_2)
newSudoku = Sudoku(inputString)
newSudoku.display(newSudoku.infer_assignment())
print('------------------------------\n')
print("Grid 3\n")
inputString = convertToString(matrix_3)
newSudoku = Sudoku(inputString)
newSudoku.display(newSudoku.infer_assignment())
print('------------------------------\n')
print("Grid 4\n")
inputString = convertToString(matrix_4)
newSudoku = Sudoku(inputString)
newSudoku.display(newSudoku.infer_assignment())
print('------------------------------\n')
print("Grid 5\n")
inputString = convertToString(matrix_5)
newSudoku = Sudoku(inputString)
newSudoku.display(newSudoku.infer_assignment())
print('------------------------------\n')
print("Grid 6\n")
inputString = convertToString(matrix_6)
newSudoku = Sudoku(inputString)
newSudoku.display(newSudoku.infer_assignment())




userChoice = input("Choose from the following grids to run sudoku solver\n")
s = ""
if userChoice == "Grid 1":
    s = convertToString(matrix_1)
    sudoku = Sudoku(s)
elif userChoice == "Grid 2":
    s = convertToString(matrix_2)
    sudoku = Sudoku(s)
elif userChoice == "Grid 3":
    s = convertToString(matrix_3)
    sudoku = Sudoku(s)
elif userChoice == "Grid 4":
    s = convertToString(matrix_4)
    sudoku = Sudoku(s)
elif userChoice == "Grid 5":
    s = convertToString(matrix_5)
    sudoku = Sudoku(s)
elif userChoice == "Grid 6":
    s = convertToString(matrix_6)
    sudoku = Sudoku(s)


if args.algorithm == "ac3":
    AC3(sudoku, arc_heuristic=dom_j_up)
    sudoku.display(sudoku.infer_assignment())

elif args.algorithm == "backtracking":
    backtracking_search(sudoku, select_unassigned_variable=mrv, inference=forward_checking)
    sudoku.display(sudoku.infer_assignment())

elif args.algorithm == "both":
        AC3(sudoku, arc_heuristic=dom_j_up)
        print("-------------Arc Consistency---------------")
        sudoku.display(sudoku.infer_assignment())
        print("-------------backtracking---------------")
        backtracking_search(sudoku, select_unassigned_variable=mrv, inference=forward_checking)
        sudoku.display(sudoku.infer_assignment())






























