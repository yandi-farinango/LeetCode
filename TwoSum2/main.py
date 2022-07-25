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
This problem requires us to use
CONSTANT extra space 
b/c of this 
we wont be able to use our previous hashmap solution

So... 
We can use two-pointers!!

We are told nums is SORTED

We can set our pointers to reference 
both ends of nums array 

If we add first number + last number 
and ans is > TARGET 
we know we've gone too far, 
and we can adjust 
end pointer by moving left 
as we move left, our next number will be smaller 

Now if we add right + left pointer 
and ans is < TARGET
we know our LEFT pointer is too small 
We can adjust by shifting pointer right, 
to a greater number 

We do this until rightPointer + leftPointer = Target
"""


class Solution(object):
    def twoSum(self, nums, target):
        # initialize pointers at opposite ends
        leftPointer, rightPointer = 0, len(nums) - 1

        while leftPointer < rightPointer:
            sum = nums[leftPointer] + nums[rightPointer]

            if sum < target:
                leftPointer += 1
            elif sum > target:
                rightPointer -= 1
            # else sum == target
            else:
                # problem specifically asked to return indices
                # added by one
                # i.e first index is considered one,
                # not zero
                return [leftPointer + 1, rightPointer + 1]



if __name__ == '__main__':
    nums = [1, 3, 4, 5, 7, 11]
    target = 9

    print(Solution().twoSum(nums, target))