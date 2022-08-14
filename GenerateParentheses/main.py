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
Since we'll be repeatedly adding parentheses, 
We can solve this recursively 

We'll need to know the following rules:
    *** A well-formed pair can be described when 
        openCount == closeCount == n
    *** Only add open in openCount < n 
    *** Only add close is closeCount < open 


We'll use two stacks:
    res - where we'll append combinations to 
    stack - which we will use to form combinations; 

We'll define a fn, backtrack, 
which accepts parameters(openCount, closeCount)

within our fn
We'll implement the rules stated above 

Rule 1
if openCount == closeCount == n:
we've created a well-formed combination, append "".join(stack) to our final result 

Rule 2
if openCount < n
we'll append open to our STACK

we recursively call backtrack
and increment open count 
    backtrack(openCount + 1, closeCount)

    (*)

Rule 3
if closeCount < openCount 
we'll append close to our STACK

we recursively call backtrack
and increment closeCount
    backtrack(openCount, closeCount + 1)

    (*)

    (*) we'll want to pop() after every recursive call as this is how the algo will 
    continuously form different combinations 


we'll pass initial value backtrack(0,0) for recursive call

return res
"""


class Solution(object):
    def generateParenthesis(self, n):

        stack = []
        res = []

        def backtack(openCount, closeCount):
            # baseCase
            if openCount == closeCount == n:
                # joining stack together and appending to res
                res.append("".join(stack))
                return

            if openCount < n:
                stack.append("(")

                backtack(openCount + 1, closeCount)
                # we want to pop from our stack every time we do our recursive call
                stack.pop()

            if closeCount < openCount:
                stack.append(")")
                backtack(openCount, closeCount + 1)
                stack.pop()

        # we pass in 0 for initial open close count
        backtack(0, 0)

        return res





if __name__ == '__main__':

    n = 3
    # n2 = 1

    print(Solution().generateParenthesis(n))
    # print(Solution().generateParenthesis(n2))
