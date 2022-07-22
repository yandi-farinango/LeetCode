"""
Determine if a 9x9 Sudoku board is valid

Only filled in cells need to be validated
according to the following:
    Each row must contain digits 1-9 w/o repetition
    Each col must contain digits 1-9 w/o repetition
    Each 3x3 subBox must contain digits 1-9 w/o repetition
"""
import collections


class Solution(object):
    def isValidSudoku(self, board):
        # Creating hashsets for cols, rows, squares
        # we use collections.defaultdict(set)

        # The tricky thing here is why we use collections.defaultdict(set)
        # We'll use defaultdict(set)
        # b/c we'll be using a SET
        # for our subSquare dictionary KEY

        cols = collections.defaultdict(set)
        rows = collections.defaultdict(set)
        squares = collections.defaultdict(set)

        for r in range(9):
            for c in range(9):
                # first check if position is empty
                if board[r][c] == ".":
                    continue
                # check if board[r][c] value exists in row[r]
                # check if board[r][c] value exists in col[c]

                # check if board[r][c] value exists
                # in subSquare[  (r//3, c//3)  ]

                # subSquare keys are sets!!
                # This is why we used defaultdict(set) above
                # Also, when we do //
                # we are doing integer division
                # where our answer will be rounded down
                # to nearest whole number

                if(board[r][c] in rows[r] or
                   board[r][c] in cols[c] or
                   board[r][c] in squares[(r // 3, c //3)]):
                    return False

                # Similar to like-problems
                # if we do not return False above,
                # we append, or in this case -add,
                # to our dictionary
                cols[c].add(board[r][c])
                rows[r].add(board[r][c])
                squares[(r//3, c//3)].add(board[r][c])
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

