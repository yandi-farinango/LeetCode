"""
Given integer array nums
and an integer k
return the kth largest element in the array

Must run in O(n)
"""

"""
To solve this problem, 
We're going to implement a quick select algorithm 

We want to get our target_index
target_index = len(nums) - k

The for quick select, 
we have a pointer p, 
and a pivot 

we are going to traverse through nums 
and partition nums 
such that all numbers less than pivot 
are stored in the left portion of nums array 

We'll have this run recursively, 

to set up our recursive function, 
we're going to pass (left, right)
our pivot will be set = nums[right]
and we'll have our p pointer set to left, 

for the partition
for i in range len(nums)
swap nums[p] with nums[i]

after our partition,
we'll want to swap p and pivot 

Recursive Calls 
if target_index < p
we want to search down 
we can search down by adjusting our right pointer 
adjust pointer(left, p - 1)

if target_index > p
we want to search up 
we can search up by adjusting the left pointer 
adjust left pointer (p + 1, right)

if p == target_index
return nums[p]

"""


class Solution(object):
    def findKthLargest(self, nums, k):

        target_index = len(nums) - k

        def quickSelect(left, right):
            pivot, p = nums[right], left

            # partition
            for i in range(left, right):
                if nums[i] <= pivot:
                    # swap nums
                    nums[i], nums[p] = nums[p], nums[i]

                    # increment p
                    p += 1

                    # swap pivot and p
            nums[p], nums[right] = nums[right], nums[p]

            if target_index < p:
                # search down by adjusting our right pointer p-1
                return quickSelect(left, p - 1)

            elif target_index > p:
                # search up by adjusting our left pointer p+1
                return quickSelect(p + 1, right)

            else:
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
