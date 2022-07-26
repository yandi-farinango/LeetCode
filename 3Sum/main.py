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

        res = []

        nums.sort()

        for idx, val in enumerate(nums):
            # if were not at the first index
            # and our value is = previous value,        **previous val is represented as nums[idx - 1]
            # we continue
            if idx > 0 and val == nums[idx - 1]:
                continue

            # from here we can take twoSum2 approach
            # on the remaining portion of nums array
            # begining at idx + 1
            # ending at len(nums) - 1
            left, right = idx + 1, len(nums) - 1

            while left < right:
                threeSum = val + nums[left] + nums[right]

                # if our threeSum is too large
                # decrease by shifting right pointer

                # if our threeSum is too small
                # increase by shifting left pointer
                if threeSum > 0:
                    right -= 1
                elif threeSum < 0:
                    left += 1
                else:
                    res.append([val, nums[left], nums[right]])

                    # we may have other solutions
                    # that would work w/ a different j
                    # so we need to shift our left pointer
                    left += 1

                    # but we want to again ignore duplicates
                    # so we also shift our left pointer on duplicates
                    # but we never want left pointer to be shifter < right
                    while nums[left] == nums[left - 1] and left < right:
                        left += 1

        return res



if __name__ == '__main__':
    nums = [-1, 0, 1, 2, -1, -4]

    print(Solution().threeSum(nums))
