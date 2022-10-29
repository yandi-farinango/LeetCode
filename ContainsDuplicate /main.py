"""
Contains Duplicate

Given an integer array, nums,
return true if nums contains duplicate

"""

"""
To solve this,
we'll initialize a set

we'll traverse num in nums
if num not already in numSet,
    we'll add num to numSet
else: 
    return True 

return False 
"""

class Solution(object):
    def containsDuplicate(self, nums):
        numSet = set()

        for num in nums:
            if num not in numSet:
                numSet.add(num)
            else:
                return True
        return False


if __name__ == '__main__':
    nums = [1, 2, 3]

    print(Solution().containsDuplicate(nums))
