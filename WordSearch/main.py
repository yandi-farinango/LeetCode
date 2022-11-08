"""
Given an m x n grid of chars
And a word,

Return TRUE if the word
exists in chars grid

"""


class Solution(object):
    def exist(self, board, word):
        pass


if __name__ == '__main__':
    board = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
    word = "ABCCED"

    print(Solution().exist(board, word))
