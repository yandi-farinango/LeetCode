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
        k = len(nums) - k

        def quickSelect(left, right):
            pivot, p = nums[right], left

            for i in range(left, right):
                if nums[i] <= pivot:
                    nums[p], nums[i] = nums[i], nums[p]
                    p += 1

            nums[p], nums[right] = nums[right], nums[p]

            if p > k:
                return quickSelect(left, p - 1)

            elif p < k:
                return quickSelect(p + 1, right)

            else:
                return nums[p]

        return quickSelect(0, len(nums) - 1)


if __name__ == '__main__':
    nums = [3, 2, 1, 5, 6, 4]
    k = 2

    print(Solution().findKthLargest(nums, k))
