"""
Given an m x n grid of chars
And a word,

Return TRUE if the word
exists in chars grid

The word can exist within the grid
either horizontally, vertically, or both
But we do want to ensure the word
can be constructed
using only neighboring cells

"""

"""
We're going to solve this problem 
recursively with backtracking

For each position in the grid
we want to look at a char's neighbors 
to determine if we can find a neighbor 
with the respective char in word 
we are looking for 

As we traverse chars in the grid, 
we'll want to be moving along the path 
of chars matching chars in word 
BUT, we dont want to revisit a particular char 

To keep track of which chars we've visited, 
we can use a set 
and as we move along chars in grid 
we can check if a char exists in our set 
ie we've already visited the char 

Recursively, we'll be checking the 
neighbors for each position in our grid 
and we'll be checking for a particular char in word 
we'll call this word[index]

So, we'll want to set up our recursive function 
to take in row, col representing the position 
and index representing word[index]

def backtracking(row, col, index)

Our base case
if i == len(word)
ie we've reached the final char in word 
we've found the word! 
Return True 

If we move out of bounds 
ie row < 0 or col < 0
or row >= number of rows 
or col >= number of cols 
or word[index] != board[r][c] ie we've found the wrong char 
or (r, c) in set ie we're trying to visit a cell we've already visited 

Return FALSE 


For each position, matching the respective word[index]
we'll want to add the position to our set 
such that we wont visit the same position twice 

We want to recursively look at all 4 adjacent positions 
for a particular word[index]

After we've moved along word[index], 
we can remove (r,c) from our visited set

and return ans 

We can do our main recursive call outside the recursive function 
looking through r in range rows
c in range cols 
"""


class Solution(object):
    def exist(self, board, word):
        # get dimensions
        rows, cols = len(board), len(board[0])

        # initialize set
        visited = set()

        def backtracking(r, c, index):
            # base case
            if index == len(word):
                return True

            # return False Base Case
            if (r < 0 or c < 0 or
                r >= rows or c >= cols or
                word[index] != board[r][c] or
                (r, c) in visited):
                return False

            # add (r, c) to visited set to keep track of visited positions
            visited.add((r, c))

            ans = (backtracking(r + 1, c, index + 1) or
                   backtracking(r - 1, c, index + 1) or
                   backtracking(r, c + 1, index + 1) or
                   backtracking(r, c - 1, index + 1))

            visited.remove((r, c))

            return ans

        for r in range(rows):
            for c in range(cols):
                if backtracking(r, c, 0):
                    return True

        return False


if __name__ == '__main__':
    board = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
    word = "ABCCED"

    print(Solution().exist(board, word))
