"""
Given an integer array nums
that may contain duplicates

return all possible subsets

The solution must NOT contain
duplicate subsets

"""

"""
We'll be solving this recursively 

At each index, we have the decision
whether to include nums[index]

we'll be making this decision recursively 
so for setting up our recursive function 
we'll be passing in 
def recursive(index, subset)

For our base case 
if index > len(nums):
ans.append(subset)
return 

for the decision to include nums[index]
subset.append(nums[index])
and we do our recursive call on 
recursive(index + 1, subset)

for the decision NOT TO include nums[index]
we'll pop from our subset 
subset.pop()

Our solution must not contain duplicate subsets 

To ensure our solution doesnt contain duplicate subsets 
we'll shift our pointer 
while index + 1 < len(nums) and index + 1 == nums[index]
index += 1 

and do our recursive call 
recursive(index + 1, subset)

We'll call our recursive function 
recursive(0, [])

and return ans 
"""


class Solution(object):
    def subsets2(self, nums):

        # initialize ans
        ans = []

        # sort nums
        nums.sort()

        def backtracking(index, subset):
            if index == len(nums):
                ans.append(subset[::])
                return

            # decision to include nums[index]
            subset.append(nums[index])
            # recursive call
            backtracking(index + 1, subset)

            # decision to NOT include nums[index]
            subset.pop()

            while index + 1 < len(nums) and nums[index + 1] == nums[index]:
                index += 1

            # recursive call
            backtracking(index + 1, subset)

        backtracking(0, [])

        return ans


if __name__ == '__main__':
    nums = [1, 2, 2]

    print(Solution().subsets2(nums))
