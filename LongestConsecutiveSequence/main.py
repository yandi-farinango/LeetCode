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

We create a set from nums array 

And as were iterating through the array, 
we check if n - 1 is in numSet

if n-1 is NOT in numset, 
we can say it is the START of a sequence

Now, if we're at the start of a sequence, 
we declare a counter, length, 

length will be updated if, 
n + length exists in our set

we'll update maxLength 
to return the longest sequence length
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
                length = 0
                # checking if n + length exists in our set
                # n + length is a reference to our next consecutive numbers
                while (n + length) in numSet:
                    length += 1
                # Updating LONGEST
                longest = max(length, longest)

        return longest


if __name__ == '__main__':
    nums1 = [100, 4, 200, 1, 3, 2]
    nums2 = [0, 3, 7, 2, 5, 8, 4, 6, 0, 1]

    print(Solution().longestConsecutive(nums1))
    print(Solution().longestConsecutive(nums2))
