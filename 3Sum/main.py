"""
Given an integer array, nums
return ALL the triplets
nums[i], nums[j], nums[k]

such that
    i != j
    i != k
    j != k

    nums[i] + nums[j] + nums[k] == 0

Solution must not
contain duplicate triplets

    Ex:
    nums = [-1, 0, 1, 2, -1, -4]
    output = [[-1, -1, 2], [-1, 0, 1]]
"""

"""
If we sort nums,

"""


class Solution(object):
    def threeSum(self, nums):

        res = []
        nums.sort()

        for i, a in enumerate(nums):
            if i > 0 and a == nums[i - 1]:
                continue

            left, right = i + 1, len(nums) -1

            while left < right:
                threeSum = a + nums[left] + nums[right]

                if threeSum > 0:
                    right -= 1
                elif threeSum < 0:
                    left += 1
                else:
                    res.append([a, nums[left], nums[right]])

                    left += 1
                    while nums[left] == nums[left - 1] and left < right:
                        left += 1
        return res



if __name__ == '__main__':
    nums = [-1, 0, 1, 2, -1, -4]

    print(Solution().threeSum(nums))
