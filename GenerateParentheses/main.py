"""
Given int, n,

Write a fn to generate
all combinations of well-formed parentheses

    Ex: n = 3
        output = ["((()))","(()())","(())()","()(())","()()()"]

            * we want to return ALL COMBINATIONS
            having 3-PAIRS
            of well-formed parentheses
"""


"""
From n, we can deduce, 
We will need 3-open parentheses 
and 3-closed parentheses 
to have a well-formed set 

Another thing we can deduce is
We must start w/ an open parentheses 
    * no well-formed pair can start w/ closed )(

Another thing we can see is 
that we can only add closing parentheses 
If the count of our open parentheses is greater than close 
    *   (() - We can add close here b/c open count = 2; close count = 1
        ()) - THIS DOESNT WORK b/c open count = 1; close count = 2
        

So since we have a lot of repeated decisions 
We can solve this problem recursively 

    *** Only add open if open count < n 
    *** only add closed if closed count < open count 
    *** STOP adding parentheses when open count == close count == n 
    
"""

class Solution(object):
    def generateParenthesis(self, n):

        stack = []
        res = []

        def backtack(openCount, closeCount):
            # baseCase
            if openCount == closeCount == n:
                # joining into one string and appending to res
                res.append("".join(stack))
                return

            if openCount < n:
                stack.append("(")

                # we append
                # and then we do our recursive call
                # we increase our openCount
                backtack(openCount + 1, closeCount)
                # we want to pop from our stack
                # every time we do our recursive call
                stack.pop()

            if closeCount < openCount:
                stack.append(")")
                backtack(openCount, closeCount + 1)
                stack.pop()

        # we pass in 0 for initial open close count
        backtack(0,0)

        return res





if __name__ == '__main__':

    n = 3
    # n2 = 1

    print(Solution().generateParenthesis(n))
    # print(Solution().generateParenthesis(n2))
