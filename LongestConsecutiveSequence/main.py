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
We can use a set! 

We can iterate through nums 
and check if n-1 exists in our set 
        
if n-1 does NOT exist, 
we know n can be considered the START
of a sequence 

Once we've determined n is the start of a sequence, 
we can have a counter for length 
that will be incremented while n + length exists in our sequence 
    (n+length is basically a reference to our next consecutive numbers)
    
To return MAX LENGTH, 
we have to remember to declare a maxLength variable prior to our loops, 
our maxLength variable will continuously get updated 
as we calculate our lengths

we return maxLength
"""

class Solution(object):
    def longestConsecutive(self, nums):

        # Create set from nums
        nums = set(nums)

        maxLength = 0

        for n in nums:
            # determining if n is the START of a sequence
            # n is the START of a sequence
            # if n-1 does NOT exist in our set
            if (n - 1) not in nums:
                # counter for length
                length = 0

                # increment length while
                # next consecutive number exits in our set
                while (n + length) in nums:
                    length += 1

            # updating maxLength
            maxLength = max(length, maxLength)

        return maxLength


if __name__ == '__main__':
    nums1 = [100, 4, 200, 1, 3, 2]
    nums2 = [0, 3, 7, 2, 5, 8, 4, 6, 0, 1]

    print(Solution().longestConsecutive(nums1))
    print(Solution().longestConsecutive(nums2))
