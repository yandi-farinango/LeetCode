"""
Integer array NUMS sorted in ascending order w DISTINCT values

Prior to being passed, NUMS may possibly be rotated
at unknown pivot index K    1<=K<=nums.length

Given array NUMS after possible rotation,
and an integer TARGET

return index of TARGET
if it is in nums
-1 if not in nums

    **Ex
    [0, 1, 2, 4, 5, 6, 7]

    rotated at pivot index 3
    [4, 5, 6, 7, 0, 1, 2]


"""

"""
Nums is:
    sorted in ascending order 
    then, possibly rotated at an unknown index 
    
    ex: [0,1,2,4,5,6,7] -> [4,5,6,7,0,1,2]
    rotated at pivot index 3
    
We can see nums can be divided into two sections 
Left section -> larger numbers 
Right section -> smaller numbers 

We use two pointers 
set at left = 0 
right = len(nums) - 1

Our first step would be to determine which section we need to search

if nums[left] <= nums[mid]

We know that our MID corresponds to our LEFT portion 

    if we are in the LEFT portion 
    
    and our target > nums[mid] or target < nums[left]
    we have to search RIGHT 
    
    else search LEFT 
    
if we know that our MID corresponds to our RIGHT portion

    if we are in the RIGHT portion 
    
    and our target < nums[mid] or target > nums[right]
    we have to search LEFT 
    
    else search RIGHT
    
return -1 
"""


class Solution(object):
    def search(self, nums, target):
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            # return mid
            if target == nums[mid]:
                return mid

            # check which section we are in

            # left portion
            if nums[left] <= nums[mid]:
                if target > nums[mid] or target < nums[left]:
                    # search left
                    left = mid + 1
                else:
                    # search right
                    right = mid - 1

            # right portion
            else:
                if target < nums[mid] or target > nums[right]:
                    # search right
                    right = mid - 1
                else:
                    # search left
                    left = mid + 1

        return -1


if __name__ == '__main__':
    nums = [4, 5, 6, 7, 0, 1, 2]
    nums2 = [1]
    nums3 = [5, 1, 3]
    nums4 = [3,1]

    target = 0
    target2 = 3
    target3 = 0
    target4 = 2
    target5 = 1

    print(Solution().search(nums, target))
    print(Solution().search(nums, target2))

    print(Solution().search(nums2, target3))

    print(Solution().search(nums3, target4))

    print(Solution().search(nums4, target5))
