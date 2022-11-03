"""
Given an integer array nums
that may contain duplicates

return all possible subsets

The solution must NOT contain
duplicate subsets

"""

"""
We're going to solve this recursively 
For recursive problems, 
its helpful to visualize 
the decision tree 
- included in drawing.png 

Similar to Subsets1 
for each index 
we have a choice 
whether to include 
nums[index]

For our solution, 
we'll initialize ans = []

we do NOT want our final solution 
to include duplicate subsets 

To do this, 
we can sort our array 
and, 
for every nums[index]
if it is a duplicate, 
we'll skip over the index 


we'll set up our recursive function 
def recursive(index, subset)4

# BASE CASE 
if i == len(nums):
ans.append(subset[::])
return 


For our recursive logic 

We have the decision to include nums[index]
    we'll append nums[i] to our subset
    and we do our recursive call on the next index 
    recursive(i + 1, subset)
    
    
we'll pop nums.pop()
    
for the decision to  NOT include nums[index]
But we also have to make sure i + 1 is not a duplicate 
we can say 
while i + 1 < len(nums) and nums[i] == nums[i + 1]
i += 1 

    and do a recursive call 
recursive(i + 1, subset)

we can call our recursive function 
passing in 0 as starting index and empty list 
"""


class Solution(object):
    def subsets2(self, nums):

        # initialize ans
        ans = []

        nums.sort()

        def backtracking(index, subset):

            # base case
            if index == len(nums):
                ans.append(subset[::])
                return

            # decision to include nums[index]
            subset.append(nums[index])
            # recursive call
            backtracking(index + 1, subset)

            # decision NOT TO include nums[index]
            subset.pop()

            while index + 1 < len(nums) and nums[index] == nums[index + 1]:
                index += 1

            # recursive call
            backtracking(index + 1, subset)

        backtracking(0, [])

        return ans


if __name__ == '__main__':
    nums = [1, 2, 2]

    print(Solution().subsets2(nums))
