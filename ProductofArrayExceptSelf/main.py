"""
Given an integer array nums
return an array, answer,
such that answer[i]
is equal to
the product of all elements of nums
EXCEPT nums[i]

Ex:
nums = [1,2,3,4]
outPut = [24,12,8,6]
"""

"""
We can calculate pre-fix products, 
multiply by post-fix products
final answer should be product of nums 
except nums[i]

We can iterate through nums 2x 

First Pass
We'll iterate through nums 
and store pre-fix products in outPut array 

Second Pass 
We'll iterate through array in REVERSE
calculate post-fix
and multiply against
pre-fix products already in our outPut array 
"""


class Solution(object):
    def productExceptSelf(self, nums):
        # declare outPut array initially w 1s
        outPut = [1] * len(nums)

        # we'll start w/ default prefix 1
        prefix = 1
        for i in range(len(nums)):
            outPut[i] = prefix
            # updating prefix
            prefix *= nums[i]

        postfix = 1
        # iterating through nums in reverse
        for i in range(len(nums) - 1, -1, -1):
            # update outPut w postfix product
            outPut[i] *= postfix
            # update postfix
            postfix *= nums[i]
        return outPut


if __name__ == "__main__":
    nums = [1, 2, 3, 4]

    print(Solution().productExceptSelf(nums))
