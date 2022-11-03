"""
Given an array nums
of distinct integers
return all the possible permutations

You can return ans in any order

"""

"""
We know 
if we have three vals 
our permutation 
has three positions, 
__, __, __

    - For our first position, 
    we have three vals we can choose from 
    
    - For our second position, 
    we now only have 2 vals we can choose from 
    ie we're already using one of the vals in position1
    
    - For our third position, 
    we only have 1 val we can choose from 

We can calculate the number of permutations we will have 
3 * 2 * 1 = 6

For recursive backtracking problems, 
its helpful to draw out the decision tree 
included in decision.png 

we'll initialize ans = []
where we'll be appending our permutations 

For our solution, 
we're going to be simplifying 
each permutation of numbers 
into a subproblem 
in which we pop the 0th number 
now are left with only 2 numbers to find the permutation for 
we continue down our decision tree, 
popping the 0th number 
until we reach our base case, 
where we are only looking for the permutation for 1 number 

# base case 
if len(nums) == 1
return [nums[:]]

We want to go through 
i in range(len(nums))

we'll be popping off the 0th number 

and get the permutations 
of the remaining values 

we get these permutations with a recursive call 
perms = self.permut(nums)

for each permutation we get from our recursive call 
we want to append the value that we removed to the end of the list 

after we've appended the previously removed value, 
we can add both permutations to our ans 

also 
we'll have to append the element we removed
back into nums 

return ans

"""


class Solution(object):
    def permute(self, nums):

        # initialize ans
        ans = []

        # base case
        if len(nums) == 1:
            return [nums[:]]

        for i in range(len(nums)):
            # pop the 0th index
            num = nums.pop(0)

            # get the permutation of the remaining vals
            permutations = self.permute(nums)

            for permutation in permutations:
                # append num to the end of permutations
                permutation.append(num)

            # append permutations to ans
            ans.extend(permutations)

            nums.append(num)

        return ans


if __name__ == '__main__':
    nums = [1, 2, 3]

    print(Solution().permute(nums))
