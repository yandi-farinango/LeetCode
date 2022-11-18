"""
Given an integer array, nums,
of unique elements
return all possible subsets

The solution must
not contain duplicate sets

Return solution in any order

    Ex: nums = [1,2,3]
        output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]

        nums = [0]
        output: [[], [0]]

"""

"""
To solve, 
we'll have to implement backtracking 

When solving backtracking problems, 
its helpful to draw out 
the decision tree
drawing included in drawing.png 


To code the backtracking solution, 

we'll initialize ans = []
where we will be appending all subsets 

we'll also initialize subset = []
where we will using to form subsets 

we'll set up our backtracking function 
passing in i
which corresponds to the index 
of the value 
we are making the decision on 
def dfs(i)

our base case 
if i >= len(nums)
we know that our recursive function is now out of bounds 
ie we've gone through all each index
we append a copy of our subset list to ans

we can say if i >= len(nums)
ans.append(list(subset))
return 


To set up the rest of the recursive function 
we'll have to implement the decision whether to include nums[i]

the decision to include nums[i] can be coded 
    subset.append(nums[i])
    
    We'll be making this decision for every index 
    so this is where we'll have a recursive call 
    dfs(i + 1)

the decision to not include nums[i] can be coded 
    we'll remove the element 
    we just appended to our subset
    subset.pop()
    
    this is also done recursively for every index 
    so we make another recursive call 
    dfs(i + 1) 

we'll call our dfs function 
starting with the 0th index 
dfs(0)

return ans 

"""


class Solution(object):
    def subsets(self, nums):

        # initialize ans
        ans = []

        # initialize subset
        subset = []

        # recursive function set to take in an index
        def dfs(index):
            # if our index is out of range, we've gone through every index in nums
            if index >= len(nums):
                ans.append(subset[::])
                return

            # decision to include nums[index]
            subset.append(nums[index])
            dfs(index + 1)

            # decision NOT to include nums[index]
            subset.pop()
            dfs(index + 1)

        dfs(0)

        return ans

    def subsetsSolution2(self, nums):
        ans = []

        def backtracking(index, subset):
            if index >= len(nums):
                ans.append(subset[::])
                return

            # decision to include nums[index]
            subset.append(nums[index])
            # recursive call
            backtracking(index + 1, subset)

            # decision NOT to include nums[index]
            subset.pop()
            backtracking(index + 1, subset)

        backtracking(0, [])

        return ans


if __name__ == '__main__':
    nums = [1, 2, 3]

    print(Solution().subsets(nums))
    print(Solution().subsetsSolution2(nums))
