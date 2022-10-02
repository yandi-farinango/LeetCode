"""
We are asked to determine wether a given Target
exists within an m x n matrix

We are told
integers are sorted left -> right
integers are sorted top -> bottom
"""

"""
We can solve this efficiently using binary search 
The tricky part here coding the matrix traversal 

We'll start by looking at rows
we initialize our pointers on opposite ends 

top pointer = 0 

bottom pointer = len(matrix) - 1

Here we can do binary search 
while left < right:
    we calculate mid

    if our target < mid; we shift our bottom pointer DOWN 
    if our target > mid; we shift our top pointer UP

    ELSE WE BREAK!

    We do a check in case we broke on the number not existing...
    if not(top <= bottom):
    return False 

    When we break, we know have the row, col where our Target value may lie 

    We identify row as (top + bottom)//2

    Now that we've identified this row, 
    we can set two more pointers
    left, right 

    left initialized = 0
    # right initialized at matrix[0] b.c we will be traversing through the COL 
    right initialized len(matrix[0]) - 1

    we do the same binary search 

    return true 
return False 
"""

class Solution(object):
    def searchMatrix(self, matrix, target):

        rows, cols = len(matrix), len(matrix[0])

        # We start seraching through rows
        top, bottom = 0, rows - 1

        while top <= bottom:
            mid = (top + bottom) // 2

            # if our target > last val in the row,
            # we want to search UP
            if target > matrix[mid][-1]:
                top = mid + 1
            # if our target < first val in the row
            # we want to search DOWN
            elif target < matrix[mid][0]:
                bottom = mid - 1
                # we might be in the right row
            else:
                break

                # get the right row
        mid_row = (top + bottom) // 2

        # Search through the row
        left, right = 0, cols - 1

        while left <= right:
            mid_col = (left + right) // 2

            # if target > mid_col shift left UP
            if target > matrix[mid_row][mid_col]:
                left = mid_col + 1

            # if target < mid_col shift right DOWN
            elif target < matrix[mid_row][mid_col]:
                right = mid_col - 1

            elif target == matrix[mid_row][mid_col]:
                return True

        return False

if __name__ == '__main__':

    matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
    target = 13

    matrix2 = [[1]]
    target2 = 1

    print(Solution().searchMatrix(matrix, target))
    print(Solution().searchMatrix(matrix2, target2))

