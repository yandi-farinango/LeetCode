"""
Given sorted array, nums
of unique elements
return the min element in the array

nums is rotated between 1 and n times

Ex: [0, 1, 2, 4, 5, 6, 7]
    [7, 0, 1, 2, 4, 5, 6] rotated 1x
    [6, 7, 0, 1, 2, 4, 5] rotated 2x
    [4, 5, 6, 7, 0, 1, 2] rotated 4x

    MUST RUN IN O(log n) <- BINARY SEARCH

"""

"""
We know we area going to have to run binary search
to solve this problem in O(log n) time

To set up our binary search we're going to have
    Left pointer 
    Right pointer 
    Mid 


notice, 
when nums array is rotated, 
we now have two "portions" 
    Left portion <- will contain larger numbers in ascending order 
    Right portion <- will contain smaller numbers in ascending order
    [4, 5, 6, 7,            0, 1, 2]
    

We set up our binary search 
Left pointer = 0 
Right pointer = len(nums)-1 

mid = (left + right) //2 

We'll want to check whether our mid value 
corresponds to 
    Left portion or 
    Right portion 


If num[left] <= nums[mid]
    our mid value corresponds to our LEFT portion 
        Ex: [4, 5, 6, 7,
        7 corresponds to LEFT PORTION 
        
    If our mid corresponds to the LEFT portion, 
    we'll want to search RIGHT
    Right portion contains smaller numbers 
        Ex: 0, 1, 2]


If num[left] <= nums[mid] is FALSE 
    our mid value corresponds to our RIGHT portion 
    in which case we'll want to search LEFT 
    
    portions are in ascending order 
    so the smallest value is going to be 
    the left-most number of the right portion
        Ex: 0, 1, 2] <- 0 is the smallest value, leftmost value 

"""

class Solution(object):
    def findMin(self, nums):
        left, right = 0, len(nums) - 1

        # ans placeholder
        ans = nums[right]

        while left <= right:

            # if we ever get to a point where we are SORTED
            # i.e nums[left] < nums[right]
            # we can update ans to the left-most number
            if nums[left] < nums[right]:
                ans = min(ans, nums[left])
                break

            mid = (left + right) // 2

            # update ans
            ans = min(ans, nums[mid])

            # mid corresponds to LEFT PORTION
            if nums[left] <= nums[mid]:
                # search right
                left = mid + 1

            # mid corresponds to RIGHT PORTION
            else:
                # search left
                right = mid - 1

        return ans


if __name__ == '__main__':
    nums = [3, 4, 5, 1, 2]
    nums2 = [2, 1]

    print(Solution().findMin(nums))
    print(Solution().findMin(nums2))


