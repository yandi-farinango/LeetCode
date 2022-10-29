"""
Given integer array nums
and an integer k
return the kth largest element in the array

Must run in O(n)
"""

"""
We can solve this problem 
using quick-select algorithm 

Quick select is implemented recursively 

For quick select, 
We want to partition our nums array 
such that, 
if we pick a random pivot, ie last index in nums, 
vals LESS than our pivot are stored to the left of the partition 
vals GREATER/EQUAL to our pivot are stored to the right of the partition 


we know our kth largest element is going to be at position len - k 

since we're doing this recursively, we can just say that we've found the kth largest element 
at the point where len-k = p

we'll want to set this up recursively 
in order to do that, we'll be passing in pointers left, right 
we'll recursively set our pivot to nums[right]
our left pointer will be used to traverse the array as we compare vals at position p 

"""


class Solution(object):
    def findKthLargest(self, nums, k):

        # get target_index
        target_index = len(nums) - k

        # set recursive function
        def quickSelect(left, right):

            # initialize p, pivot
            pivot, p = nums[right], left

            # set up partition
            for i in range(left, right):
                if nums[i] <= pivot:
                    # swap val w its own position,
                    # ie val remains in its original position
                    nums[i], nums[p] = nums[p], nums[i]

                    # shift pointer
                    p += 1

            # swap pivot w p pointer position
            nums[p], nums[right] = nums[right], nums[p]

            # recursive calls
            # if target_index < p, run quickSelect on LEFT to search for a smaller index
            if target_index < p:
                # shift right p-1
                return quickSelect(left, p - 1)

            # if target_index > p; run quickSelect on RIGHT to search for a greater index
            elif target_index > p:
                # shift left p+1
                return quickSelect(p + 1, right)

            else:
                # found kth largest
                return nums[p]

        # recursive call
        return quickSelect(0, len(nums) - 1)


if __name__ == '__main__':
    nums = [3, 2, 1, 5, 6, 4]
    k = 2

    nums2 = [3, 2, 3, 1, 2, 4, 5, 5, 6]
    k2 = 4

    print(Solution().findKthLargest(nums, k))
    print(Solution().findKthLargest(nums2, k2))
