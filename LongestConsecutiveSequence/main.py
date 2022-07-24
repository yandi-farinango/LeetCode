"""
Given an unsorted array of integers, nums
return the length
of the longest consecutive elements-sequence

Must run in O(n)

Ex:
nums = [0,3,7,2,5,8,4,6,0,1]

consecutive elements-sequence = [0,1,2,3,4,5,6,7,8]

output
length = 9
"""


"""

"""


class Solution(object):
    def longestConsecutive(self, nums):

        # Create set from nums
        numSet = set(nums)

        # Variable for keeping track of longest sequence
        longest = 0

        for n in nums:
            # check if n is the start of a sequence
            # n is the start of a sequence if
            # n-1 does NOT exist in nums
            if (n - 1) not in numSet:







if __name__ == '__main__':
