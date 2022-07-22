#

# class Solution(object):
#     def maxSubArray(self, nums):
#
#         maxSub = nums[0]
#         totalSum = nums[0]
#
#         for n in nums:
#             if totalSum < n:
#                 totalSum += n
#             maxSub = max(maxSub, totalSum)
#         return maxSub


class Solution(object):
    def maxSubArray(self, nums):
        maxSub = nums[0]
        totalSum = 0

        for n in nums:
            if totalSum < n:
                totalSum += n
            maxSub = max(maxSub, totalSum)
        return maxSub

# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    nums = [-2,1,-3,4,-1,2,1,-5,4]
    print(Solution().maxSubArray(nums))


