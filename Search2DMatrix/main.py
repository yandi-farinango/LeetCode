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

Here we can do binary serach 
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

        # our first set of pointers will traverse rows
        # we'll initialize our left pointer at 0
        # and our right pointer will traverse matrix rows
        # matrix rows = len(matrix)
        top, bottom = 0, len(matrix) - 1

        while top < bottom:
            mid = (top + bottom) // 2

            # if our target is greater than last number in row mid
            # well want to shift our top pointer UP
            if target > matrix[mid][-1]:
                top = mid + 1

            # if our target is less than the FIRST number in row mid
            # we want to shift our bottom pointer DOWN
            elif target < matrix[mid][0]:
                bottom = mid - 1

            else:
                break

        # When we break,
        # our last top and bottom are cached

        if not (top <= bottom):
            return False

        # we want to get the row where our target may lie
        row = (top + bottom) // 2

        # this time we'll set our pointer to traverse through the cols
        # cols can be described by len(matrix[0])
        left, right = 0, len(matrix[0]) - 1

        while left < right:
            midpoint = (left + right) // 2

            # if our target is greater than our midpoint
            # shift left UP
            if target > matrix[row][midpoint]:
                left = midpoint + 1

            # our target is less than our midpoint
            # we want to shift our left pointer DOWN
            elif target < matrix[row][midpoint]:
                right = midpoint - 1

            else:
                return True
        return False


if __name__ == '__main__':

    matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60],[61,65,66,67]]
    target = 30

    print(Solution().searchMatrix(matrix, target))