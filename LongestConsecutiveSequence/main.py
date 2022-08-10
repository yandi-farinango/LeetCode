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
We want to return the len 
of the LongestConsecutiveSequence 

To do this, we need to identify 
What is a sequence 
i.e where a sequence begins 

If we use a convert nums to a set, 

as we iterate through n in nums 
we can check if n-1 exists in our set 

If it does not exist in our set, 
we know n can be considered the start of a sequence 

We can use a variable Length, 
that can be incremented while n + length exists in our sequence 
B/c we are incrementing length, 
we can use n + length 
as a reference to the next elements in our sequence 

We'll also have a global variable maxLen that will 
be updated w max(len, maxLen)

return maxLen
"""

class Solution(object):
    def longestConsecutive(self, nums):

        maxLen = 0

        # convert nums to a set
        numSet = set(nums)

        for n in nums:
            # if n - 1 is NOT in our numSet
            # were at the start of a sequence

            if (n - 1) not in numSet:
                length = 0

                while n + length in numSet:
                    length += 1

                maxLen = max(length, maxLen)

        return maxLen


if __name__ == '__main__':
    nums1 = [100, 4, 200, 1, 3, 2]
    nums2 = [0, 3, 7, 2, 5, 8, 4, 6, 0, 1]

    print(Solution().longestConsecutive(nums1))
    print(Solution().longestConsecutive(nums2))
