"""
Given a 1-indexed array of integers, nums, 
that is SORTED in NON-DECREASING order 

Find 2 numbers 
such that 
they add up to
a specific TARGET number

Return the indices of the two numbers, 
added by one, 
as an integer array 
of length = 2

Solution MUST use
constant extra space


    Ex: nums = [1, 3, 4, 5, 7, 11]
    TARGET = 9 
    
    ans = [3, 4]

"""


"""
We are told that the array is SORTED 

We are to find two numbers 
that add to the target 

MUST USE constant extra space 
-meaning- 
We cant use a hashamp, array, list, etc 

To solve 
We can use two pointers 
initialized on opposite ends of numbers array 

Because we are told the array is sorted 

If numbers[left] + numbers[right] > 0
    We need to shift our right pointer DOWN to a smaller number 
    
If numbers[left] + numbers[right] < 0 
    We need to shift our right pointer UP to a greater number 

We are also told there is exactly one solution 
SO... 
If none of the above conditions satisfy 
else:        
We return [left + 1, right + 1]
"""


class Solution(object):
    def twoSum(self, numbers, target):

        # initialize pointers
        left, right = 0, len(numbers) - 1

        # left will always be less than right
        while left < right:

            # first condition - if > target, we need to shift right DOWN
            if numbers[left] + numbers[right] > target:
                right -= 1

            # second condition - if numbers < target, we need to shift left UP
            elif numbers[left] + numbers[right] < target:
                left += 1

            else:
                return left + 1, right + 1

        return


if __name__ == '__main__':
    nums = [1, 3, 4, 5, 7, 11]
    target = 9

    print(Solution().twoSum(nums, target))