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
We are to return res[[]]
containing DISTINCT triplet groups
which sum together = 0 

nums may contain duplicate values 

as we're appending to res[[]]
we want to make sure
our i is DISTINCT 
so that
it wont cause us to append
duplicate triplets 


if we first SORT our array, 
before iterating through, 
we can skip repeated nums[i] values

We can use enumerate, 
to get idx, and values
and if val = nums[idx -1]
we'll know its repeated 
We'll skip if repeated 

From there, the remainder of the problem 
can be solved 
taking the twoSum2 approach 
"""


class Solution(object):
    def threeSum(self, nums):

        nums.sort()
        res = []

        for index, val in enumerate(nums):
            # skip duplicates
            if index > 0 and val == nums[index - 1]:
                continue

            left, right = index + 1, len(nums) - 1

            while left < right:
                # if our sum > 0, we need to decrease, i.e shift right pointer
                if (val + nums[left] + nums[right]) > 0:
                    right -= 1
                # if we're less than 0, we need to increase, i.e shift left pointer
                elif (val + nums[left] + nums[right]) < 0:
                    left += 1
                else:
                    res.append([val, nums[left], nums[right]])
                    left += 1

                    # we want to ignor duplicates in j and k as well
                    # so we shift our left pointer on duplicates
                    while nums[left] == nums[left - 1] and left < right:
                        left += 1
        return res



if __name__ == '__main__':
    nums = [-1, 0, 1, 2, -1, -4]

    print(Solution().threeSum(nums))
