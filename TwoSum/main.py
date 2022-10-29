"""
Given an array of integers, nums, and target
return the indices of two numbers that add up to target

We can assume there is always one solution

"""

"""
To solve this problem 
we can use a set 

well have 
numSet = set(nums)

And we'll traverse nums 

for i in range nums 

and say missing_val = abs(target - nums)

if missing_val in numSet:

return [i, nums.index(missing_val)]

"""

class Solution:
    def twoSum(self, nums, target):

        # initialize numSet
        numSet = set(nums)

        for i in range(len(nums)):
            missing_val = (target - nums[i])

            if (missing_val in numSet) and (nums.index(missing_val) != i):
                return [i, nums.index(missing_val)]


if __name__ == '__main__':
    nums = [2, 7, 11, 15]
    target = 9

    nums2 = [-1,-2,-3,-4,-5]
    target2 = -8

    print(Solution().twoSum(nums, target))
    print(Solution().twoSum(nums2, target2))










