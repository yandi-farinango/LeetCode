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

        row, col = len(matrix), len(matrix[0])

        # top -> bottom binary search
        top = 0
        bottom = row -1

        while top <= bottom:
            mid = (bottom + top) // 2

            # if target is less than mid, shift top UP
            if target > matrix[mid][-1]:
                top = mid + 1
            elif target < matrix[mid][0]:
                bottom = mid - 1
            else:
                break

        if not(top <= bottom):
            return False

        row = (top + bottom) // 2

        # right -> left binary search
        left = 0
        right = col - 1

        while left <= right:
            mid = (right + left) // 2

            if target < matrix[row][mid]:
                right = mid - 1

            elif target > matrix[row][mid]:
                left = mid + 1

            else:
                return True

        return False


class Solution2(object):
    def searchMatrix(self, matrix, target):
        row, col = len(matrix), len(matrix[0])

        top, bottom = 0, row - 1

        while top <= bottom:
            mid = (top + bottom) // 2

            # if target > than last element in mid row,
            if target > matrix[mid][-1]:
                # shift our top pointer UP
                top = mid + 1

            # if target < the first element in mid row
            elif target < matrix[mid][0]:
                # shift bottom pointer UP
                bottom = mid - 1

                # if target not > matrix[mid][-1]
                # and target not < mid[mid][0]
                # our target may lie within this row!!
            else:
                left, right = 0, col - 1

                while left <= right:
                    mid_col = (left + right) // 2

                    # if target > mid_col
                    if target > matrix[mid][mid_col]:
                        # shift left UP
                        left = mid_col + 1

                    # if target < mid_col
                    elif target < matrix[mid][mid_col]:
                        # shift Right DOWN
                        right = mid_col - 1
                    else:
                        return True

                return False



if __name__ == '__main__':

    matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60],[61,65,66,67]]
    target = 30

    matrix2 = [[1]]
    target2 = 1

    print(Solution().searchMatrix(matrix, target))
    print(Solution().searchMatrix(matrix2, target2))

    print(Solution2().searchMatrix(matrix, target))
    print(Solution2().searchMatrix(matrix2, target2))