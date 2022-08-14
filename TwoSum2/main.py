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
This solution must be solved using only constant extra space 

We are also told that the array is already SORTED 

We can use two pointers
On opposite ends of numbers array 

if numbers[left] + numbers[right] < 9 
well have to shift our left pointer up 

if numbers[left] + numbers[right] > 9 
well have to shift our right pointer down 

else * numbers[left] + numbers[right] == target

so we can return [left + 1, right + 1]
"""


class Solution(object):
    def twoSum(self, numbers, target):
        left = 0

        right = len(numbers) - 1

        while left < right:

            # shift left pointer up
            if numbers[left] + numbers[right] < target:
                left += 1

            # shift right pointer down
            elif numbers[left] + numbers[right] > target:
                right -= 1

            else:
                return [left + 1, right + 1]

        return


if __name__ == '__main__':
    nums = [1, 3, 4, 5, 7, 11]
    target = 9

    print(Solution().twoSum(nums, target))