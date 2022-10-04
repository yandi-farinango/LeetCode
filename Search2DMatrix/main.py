"""
We are asked to determine wether a given Target
exists within an m x n matrix

We are told
integers are sorted left -> right
integers are sorted top -> bottom
"""

"""
We can solve this using a binary search 

when working w/ matrix 
rows = len(matrix)
cols = len(matrix[0])

We'll first try to identify which row our target may potentailly lie 

    We'll set up our binary search to look through the rows 
    from top -> bottom 

    if our target is greater than the LAST value in the row
    search UP for larger numbers 

    elif our matrix is less than the FIRST value in the row
    search DOWN for a smaller numbers 

    else we've found a potential row!


Then we'll search through the cols of the potential row for target 
    if target > matrix[potential_row][mid_col]
    shift UP
    
    elif target < matrix[potential_row][mid_col]
    shift DOWN 
    
    else:
        We've found TARGET! Return True 
        
        
return False 
"""

class Solution(object):
    def searchMatrix(self, matrix, target):
        rows, cols = len(matrix), len(matrix[0])

        """
        Binary Search through ROWS
        """
        top, bottom = 0, rows - 1

        while top <= bottom:
            mid_row = (top + bottom) // 2

            # if our matrix is greater than the LAST value in the row
            if target > matrix[mid_row][-1]:
                # search UP for larger numbers
                top = mid_row + 1

            # if our matrix is less than the FIRST value in the row
            elif target < matrix[mid_row][0]:
                # search DOWN for a smaller numbers
                bottom = mid_row - 1

            # we've found a potential row!
            else:
                break

                # get the potential row
        potential_row = (top + bottom) // 2

        """
        Binary Search through COLS
        """

        left, right = 0, cols - 1

        while left <= right:
            mid_col = (left + right) // 2

            # if target > matrix[potential_row][mid_col]
            if target > matrix[potential_row][mid_col]:
                # shift UP
                left = mid_col + 1

            # if target < matrix[potential_row][mid_col]
            elif target < matrix[potential_row][mid_col]:
                # shift DOWN
                right = mid_col - 1
            else:
                return True

        return False

if __name__ == '__main__':

    matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
    target = 13

    matrix2 = [[1]]
    target2 = 1

    print(Solution().searchMatrix(matrix, target))
    print(Solution().searchMatrix(matrix2, target2))

