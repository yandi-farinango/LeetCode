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
Given nums, 
we are to return all triplets 
adding to 0

    Ex: nums[i] + nums[j] + nums[k] = 0
    return [  [nums[i], nums[j], nums[k]]  ]
    
Our solution must not contain duplicate triplet sets 

B/c NUMS may contain duplicates,
if we were to iterate through nums
using loops, 
AND, 
we came across a duplicate
in position nums[i], 
we would be returning duplicate triplet sets

SO, 
we know that nums[i] MUST be unique 


if we first SORT our array, 
before iterating through, 
we can skip repeated nums[i] values

SORTING also allows us to use twoSum2 
solution 
for finding n[j] and n[k]! 



"""


class Solution(object):
    def threeSum(self, nums):

        # result will be returned as [[]]
        res = []

        # we first want to sort nums array
        nums.sort()

        for index, value in enumerate(nums):
            # we don't want to re-use for n[i] position

            # if were NOT at first index
            # and our value is == to the previous
            # we ignore
            if index > 0 and value == nums[index - 1]:
                continue

            # Now we can implement our twoPointer2 sol
            # we set our pointers on remaining portion
            # of our nums array
            # if we're at idx
            # our remaining portion begins at idx + 1
            # and ends at len(nums) - 1

            left, right = index + 1, len(nums) - 1

            while left < right:
                # we don't do nums[idx] + nums[left] +...
                # b/c we are idx, val ENUMERATING in our loop
                # we can just call our val
                threeSum = value + nums[left] + nums[right]

                if threeSum > 0:
                    right -= 1
                elif threeSum < 0:
                    left += 1
                else:
                    # we've found a triplet set!
                    # append to result
                    res.append([value, nums[left], nums[right]])

                    # we want to shift our left pointer
                    # to iterate through the rest of nums
                    # and see if we potentially have other triplet groups
                    left += 1
                    # we want to find NEW triplet groups
                    # so we ignore duplicates

                    # if nums[left] is the same
                    # as nums[left] before,
                    # it is a duplicate

                    # we shift our left pointer to ignore duplicates
                    # but we also ALWAYS want our left pointer to be less than right
                    while nums[left] == nums[left - 1] and left < right:
                        left += 1
        return res



if __name__ == '__main__':
    nums = [-1, 0, 1, 2, -1, -4]

    print(Solution().threeSum(nums))
