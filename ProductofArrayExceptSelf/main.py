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
We can do this problem taking a two-pass approach

We want all the products of nums except nums[i]

That means we want prefix nums[i] * postfix nums[i]


We'll be using an output array to store prefix & postfix
and, we will return output array as our answer 



On our first pass, 
we'll be calculating prefix

We'll have a variable prefix, which will get updated
as we traverse through the array going forward 



On our second pass, 
We'll have a variable postfix, 
which will get updated as we traverse through the array going in reverse 

We will multiply our postfix 
against the respective prefix value in our output array

return outPut array        
"""


class Solution(object):
    def productExceptSelf(self, nums):
        # initial outPut array
        outPut = [1] * len(nums)

        prefix = 1
        for i in range(len(nums)):
            # outPut[i] = respective prefix
            outPut[i] = prefix
            # updating prefix
            prefix *= nums[i]

        postfix = 1
        for i in range(len(nums) - 1, -1, -1):
            # prefix, stored in output[i], is multiplied against postfix
            outPut[i] *= postfix
            # updating postfix
            postfix *= nums[i]

        return outPut


if __name__ == "__main__":
    nums = [1, 2, 3, 4]

    print(Solution().productExceptSelf(nums))
