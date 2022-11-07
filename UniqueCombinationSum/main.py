"""
NOT AN OFFICIAL LEETCODE PROBLEM

Given nums array, and a target value

This solution finds all unique combinations 
which sum to target 

numbers MAY be used more than once 
BUT, ans must NOT contain any duplicates 
"""

"""
We'll can solve this using recursion 

For each index in nums, 
we have the decision
whether to include 
nums[index] or not 

We'll also be building the combinations recursively 
and, since we're building combinations recursively, 
we'll be having a separate sum for each combination 

Since we do NOT want our solution to contain 
any duplicate combinations, 
we'll sort nums
and in our recursive logic, 
we'll continuously skip over indices 
where nums[index] == nums[index + 1]

So...
To set up our recursive function, 
we'll be passing in index, combination, sum 

We'll initialize an ans variable 
where we'll append all possible combinations 
sort nums 
and set up our recursive function 
def backtracking(index, combination, sum)

Our base case 
If sum == target, 
we want to append combination to ans 
return

if index >= len(nums) or sum > target:
return 

For the recursive logic, 

we'll be making the decision 
to include nums[i] in our combination
we'll append combination.append(nums[index])

for the decision to NOT include nums[i] in our combination,
we'll pop nums[index] from our combination 

while index > len(nums) and sum + nums[index] > target
we'll continuously increment index

"""

class Solution(object):
    def uniqueCombinationSum(self, nums, target):
        # initialize ans
        ans = []

        nums.sort()

        def backtracking(index, combination, sum):
            # base case
            if sum == target:
                ans.append(combination[::])
                return

            # base case
            if index >= len(nums) or sum > target:
                return

            # decision TO include nums[index]
            combination.append(nums[index])
            # recursive
            backtracking(index, combination, sum + nums[index])     # we dont increment index bc numbers may be used more than once

            # decision NOT TO include nums[index]
            combination.pop()

            while index > len(nums) or sum > target:
                index += 1

            backtracking(index + 1, combination, sum)

        backtracking(0, [], 0)

        return ans


if __name__ == '__main__':
    nums = [3, 6, 1, 2]
    target = 10

    print(Solution().uniqueCombinationSum(nums, target))