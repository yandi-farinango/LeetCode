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
    [7, 6, 5, 4, 0, 1, 2]


"""

"""
We can see that after rotation, 
our array can be seperated into two sections 
LEFT section contains LARGER numbers in DESCENDING order
RIGHT section contains SMALLER numbers in ASCENDING order

If we try binary search 

We'll start with our pointers initialized at
left = 0 
right = len(nums) - 1

We can get some information about our MIDPOINT 

MIDPOINT <= LEFT
MIDPOINT corresponds to our LEFT section
i.e fits with numbers in DESCENDING order from LEFT -> RIGHT 


Once we've identified how our nums array is structured

Our next step would be 
which PORTION we want to search 


IF our MID corresponds to our LEFT portion
        if TARGET > nums[mid], TARGET might lie in our RIGHT portion 
        also if TARGET < nums[left], TARGET might lie in our RIGHT PORTION
        
        we shift left pointer UP 
        left = mid + 1
        
        
        else:
        right = mid - 1 


IF our MID corresponds to our RIGHT,
        if TARGET < nums[mid], TARGET might lie in our LEFT portion 
        also if TARGET > nums[left], TARGET might lie in our LEFT portion 
        
        we shift our right pointer DOWN 
        right = mid - 1 
        
        else 
        left = mid - 1
        
"""


class Solution(object):
    def search(self, nums, target):
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            if target == nums[mid]:
                return mid

            # mid belongs to LEFT portion
            # ie LARGER numbers DESCENDING order
            if nums[left] <= nums[mid]:

                # if our MID belongs to our left
                # and if TARGET > nums[mid] TARGET might lie in our RIGHT portion
                # also if TARGET < nums[left] TARGET might lie in our RIGHT portion
                if target > nums[mid] or target < nums[left]:
                    left = mid + 1
                else:
                    right = mid - 1


            # mid belongs to RIGHT portion
            # ie SMALLER numbers ASCENDING order
            else:
                # if MID belongs to our RIGHT
                # and if TARGET > nums[mid]
                # also if target > nums[left]
                if target < nums[mid] or target > nums[left]:
                    right = mid - 1
                else:
                    left = mid + 1

        return -1


if __name__ == '__main__':
    nums = [4, 5, 6, 7, 0, 1, 2]
    nums2 = [1]

    target = 0
    target2 = 3
    target3 = 0

    print(Solution().search(nums, target))
    print(Solution().search(nums, target2))

    print(Solution().search(nums2, target3))
