"""
Given a collection of candidate numbers
And a target

Find all unique combinations
of numbers
which sum to target

Each number may only be used once
in the combination

The solution cant contain duplicates

"""

"""
For this problem, 
We dont want to include
any duplicates 

The way we can solve this is 
skipping over indices 
of the same number 

If we sort candidates array,
we'll be able to skip over 
the repeated indices 

We'll initialize ans = []

and we'll sort candidates 

For our recursive function, 
we'll be passing 
def backtracking(index, combination, sum)


"""


class Solution(object):

    def combinationSum2(self, candidates, target):

        # initialize ans
        ans = []

        candidates.sort()

        def backtracking(current, position, target):
            # base case
            if target == 0:
                ans.append(current[::])

            if target <= 0:
                return

            # initialize prev
            prev = -1
            for i in range(position, len(candidates)):
                if candidates[i] == prev:
                    continue

                # decision to include candidates[i]
                current.append(candidates[i])

                # we're going to be recursively subtracting target - candidates[i]
                backtracking(current, i + 1, target - candidates[i])

                # decision NOT to include candidates[i]
                current.pop()

                prev = candidates[i]

        backtracking([], 0, target)

        return ans


if __name__ == '__main__':
    candidates = [10, 1, 2, 7, 6, 1, 5]
    target = 8

    print(Solution().combinationSum2(candidates, 8))





