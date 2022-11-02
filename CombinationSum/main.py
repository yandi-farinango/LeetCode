"""
Given an array of distinct integers, candidates,
and a target integer, target,
return a list
of all the unique combinations
of candidates where the chosen numbers sum to target

you may return the combinations in any order

The same number may be chosen from candidates
an unlimited number of times

Two combinations are unique
if the frequency
of at least one of the chosen numbers is different

"""

"""
As with recursive problems, 
it is helpful to draw out the decision tree 
included in drawing.png 

We can see from our drawing, 
we cant have a decision tree
based on candidates, 
bc we'd end up w duplicates 

We want our decision tree to be based on 
whether to include a number or not 
and then go through the numbers in combinations 
we can do this using a pointer 
that will tell which candidate we're allowed to use 

We'll be returning a list of combinations so
we can initialize ans = []

we'll set up our recursive function 
def dfs(i, current, total)

where i is our pointer to keep track of candidate were on 
current keeps track of the current combination
total keeps track of the total sum 

Our base case
if total == target:
res.append(list(current))
return 

if i >= len(candidates) or total > target
we're out of bounds 
return 


For our recursive logic 
Our decision is based on 
whether to include candidates[i]

we do this 
current.append(candidates[i]

# Recursive call to include candidate
# i stays the same
dfs(i, current, total + candidates[i])

# Recursive call to NOT include candidate 
we pop to remove candidate,
current.pop()
and increment i 
dfs(i + 1, current, total)


our dfs call
dfs(0, [], 0)

return res
"""

class Solution(object):
    def combinationSum(self, candidates, target):
        ans = []

        def dfs(i, current, total):
            # base case
            if total == target:
                ans.append(current.copy())
                return

            # base case
            if i >= len(candidates) or total > target:
                return

            """recursive decision to include candidate """
            # append candidates[i]
            current.append(candidates[i])
            # recursive
            dfs(i, current, total + candidates[i])

            """recursive decision NOT to include candidate"""
            # pop candidates[i]
            current.pop()
            # recursive
            dfs(i + 1, current, total)  # i + 1 bc we are skipping over candidates[i]

        # recursive start
        dfs(0, [], 0)

        return ans


if __name__ == '__main__':
    candidates = [2, 3, 6, 7]
    target = 7

    print(Solution().combinationSum(candidates, target))