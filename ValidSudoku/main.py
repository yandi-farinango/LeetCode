"""
Determine if a 9x9 Sudoku board is valid

Only filled in cells need to be validated
according to the following:
    Each row must contain digits 1-9 w/o repetition
    Each col must contain digits 1-9 w/o repetition
    Each 3x3 subBox must contain digits 1-9 w/o repetition
"""


"""
This problem is very similar to eariler array problems, 
where we can add to a hashset
to determine whether a variable already exists in the hashset 

The tricky thing here is dealing w/ the subsquares 

To solve this we will do the following:
    Think of the subsquares as 3x3 grid 
    X,Y vals from 1-3
    To get this reference we will be using a SET

    our SET will (r//3, c//3)

    When we do a floor division, 
    our result is rounded down
    to the nearest whole number 

    Ex: We have 9 rows (0 - 8)
    Rows 0-2, when // by 3 
    will return 0

    Similar will happen for cols

    And so, we now have a reference to 
    our 3x3 subsquares 


Now... in order to be able to use a set as a reference 
We need to use collections.defaultdict(set)

Once we've declared our defaultdict(set), 
the logic is similar to easier problems 

We traverse through board, 
    -dont forget
    if we come across "." 
    we will simply continue

check if board[r][c] exists within the respective dict
If so we return FALSE
If not, we add to the respective dict
At the end return True

"""


import collections


class Solution(object):
    def isValidSudoku(self, board):

        # default.dict(set)
        row = collections.defaultdict(set)
        col = collections.defaultdict(set)
        squares = collections.defaultdict(set)

        # use in range(9)
        # we were given 9x9 as board size
        for r in range(9):
            # ignore "."
            for c in range(9):
                if board[r][c] == ".":
                    continue
                # checking if board[r][c] exists in either row, col, or board
                if (board[r][c] in row[r] or
                        board[r][c] in col[c] or
                        board[r][c] in squares[(r // 3, c // 3)]):
                    return False
                # adding to our dict(set)
                # if board[r][c] does not already exist
                row[r].add(board[r][c])
                col[c].add(board[r][c])
                squares[(r // 3, c // 3)].add(board[r][c])

        return True

if __name__ == '__main__':
    board1 = [["5", "3", ".", ".", "7", ".", ".", ".", "."],
             ["6", ".", ".", "1", "9", "5", ".", ".", "."],
             [".", "9", "8", ".", ".", ".", ".", "6", "."],
             ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
             ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
             ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
             [".", "6", ".", ".", ".", ".", "2", "8", "."],
             [".", ".", ".", "4", "1", "9", ".", ".", "5"],
             [".", ".", ".", ".", "8", ".", ".", "7", "9"]]

    board2 = [["8","3",".",".","7",".",".",".","."],
              ["6",".",".","1","9","5",".",".","."],
              [".","9","8",".",".",".",".","6","."],
              ["8",".",".",".","6",".",".",".","3"],
              ["4",".",".","8",".","3",".",".","1"],
              ["7",".",".",".","2",".",".",".","6"],
              [".","6",".",".",".",".","2","8","."],
              [".",".",".","4","1","9",".",".","5"],
              [".",".",".",".","8",".",".","7","9"]]

    print(Solution().isValidSudoku(board1))
    print(Solution().isValidSudoku(board2))

