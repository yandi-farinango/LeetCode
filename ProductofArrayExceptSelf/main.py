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
To calculate product of array except self, 
We'll be multiplying prefix elements * postfix elements 

We can do this efficiently by
First traversing the array 
And calculating prefix products 

And, on our second pass, 
Traverse the array in reverse
Calculating our postfix products 

and multiplying prefix * postfix 

We'll use a res [1] variable of len(nums)

and well use a prefix variable 
initially set = 1
which will be updated as we loop through 

after we've done our first pass
we'll loop through res backwards 

similar to above, 
we'll use a postfix variable 
initially set = 1
that will be updated as we loop 

return res
"""


class Solution(object):
    def productExceptSelf(self, nums):

        res = [1] * len(nums)

        # prefix variable initally set = 1
        # will be continously updated in our loop
        prefix = 1

        for i in range(len(nums)):
            res[i] = prefix
            # update prefix
            prefix *= nums[i]

        # postfix variable
        # will be contiously updated in our loop
        postfix = 1

        # looping backwards
        for i in range(len(nums) - 1, -1, -1):
            # res[i] contains prefixs
            # multiplying prefix * postfix
            res[i] *= postfix
            # update postfix
            postfix *= nums[i]

        return res


if __name__ == "__main__":
    nums = [1, 2, 3, 4]

    print(Solution().productExceptSelf(nums))
