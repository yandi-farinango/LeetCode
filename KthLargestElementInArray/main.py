"""
Given integer array nums
and an integer k
return the kth largest element in the array

Must run in O(n)
"""

"""
We are going to solve this problem 
implementing a quick-select algorithm 

Quick select will be implemented recursively 

For the quick-select function
we'll pass in a left, right pointer 

we'll initialize 
pivot = nums[right]
p = left 


"""


class Solution(object):
    def findKthLargest(self, nums, k):

        # initialize k
        k = len(nums) - k

        # set recursive function
        def quickSelect(left, right):

            # initialize p, pivot
            p, pivot = left, nums[right]

            # partition
            for i in range(left, right):
                if nums[i] <= pivot:
                    # swap nums[i], nums[p]
                    nums[i], nums[p] = nums[p], nums[i]
                    p += 1

            # swap pivot, p
            nums[p], nums[right] = nums[right], nums[p]

            # recursive calls
            # if k < p, run quickSelect on LEFT
            if k < p:
                return quickSelect(left, p - 1)

            # if k > p; run quickSelect on RIGHT
            elif k > p:
                return quickSelect(p + 1, right)

            else:
                return nums[p]

        return quickSelect(0, len(nums) - 1)


if __name__ == '__main__':
    nums = [3, 2, 1, 5, 6, 4]
    k = 2

    nums2 = [3, 2, 3, 1, 2, 4, 5, 5, 6]
    k2 = 4

    print(Solution().findKthLargest(nums, k))
    print(Solution().findKthLargest(nums2, k2))
