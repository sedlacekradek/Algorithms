"""
Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

Each row must contain the digits 1-9 without repetition.
Each column must contain the digits 1-9 without repetition.
Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.

Note:
A Sudoku board (partially filled) could be valid but is not necessarily solvable.
Only the filled cells need to be validated according to the mentioned rules.

Example 1:
Input: board =
[["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
Output: true

Example 2:
Input: board =
[["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
Output: false
Explanation: Same as Example 1, except with the 5 in the top left corner being modified to 8.
Since there are two 8's in the top left 3x3 sub-box, it is invalid.
"""


def isValidSudoku(board):
    # iterate through all cols and rows and check for duplicates
    # 1. create 3 dics (row, col, box)
    # 2. iterate through board only once and add to all 3 dics at once and check for duplicates
    # -> no need to iterate through board 3 times

    hash_map_row = {}
    hash_map_col = {}
    hash_map_box = {}

    # iterate through 2D matrix once
    y = 0
    while y < 9:
        x = 0
        while x < 9:


            # if empty, continue
            if board[y][x] == ".":
                x += 1  # don't forget +1
                continue

            # check cols
            key1 = f"{board[y][x]}inCol{y}"
            if key1 in hash_map_col:
                return False
            else:
                hash_map_col[key1] = "_"

            # check rows
            key2 = f"{board[y][x]}inRow{x}"
            if key2 in hash_map_row:
                return False
            else:
                hash_map_row[key2] = "_"

            # check boxes
            # create index for each 3x3 box (y//3, x//3)
            box_index = f"{y//3}{x//3}"
            key3 = f"{board[y][x]}in{box_index}"
            if key3 in hash_map_box:
                return False
            else:
                hash_map_box[key3] = "_"

            x += 1
        y += 1
    return True


board = [
 ["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","7",".",".",".",".","6","."]
,["1",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]
]

print(isValidSudoku(board))


board = [
 ["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]
]

print(isValidSudoku(board))