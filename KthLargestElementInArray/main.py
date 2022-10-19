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

            # initialize p pointer, pivot
            p, pivot = left, nums[right]

            # partition
            for i in range(left, right):
                if nums[i] <= pivot:
                    # swap with itself
                    nums[p], nums[i] = nums[i], nums[p]
                    # increment counter
                    p += 1

            # swap pivot at partition
            nums[p], nums[right] = nums[right], nums[p]

            # recursive calls

            # we know the kth largest lies within the left half,
            # ie in our recursive call, we set right to p-1
            if k < p:
                return quickSelect(left, p - 1)

            # we know the kth largest lies within the p + 1 partition
            elif k > p:
                return quickSelect(p + 1, right)

            # found kth largest
            else:
                return nums[p]

        # base recursive call
        return quickSelect(0, len(nums) - 1)


if __name__ == '__main__':
    nums = [3, 2, 1, 5, 6, 4]
    k = 2

    print(Solution().findKthLargest(nums, k))
