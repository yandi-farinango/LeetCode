"""
Given a list of str, Tokens,
We are to calculate the Reverse Polish Notation

Reverse Polish Notation
is a form of solving math equations

Equations are read from left -> right
When we get to an operator (+, -, *, /)
    We perform the operation
    on the previous 2 values

    ***On division***
    we want to round towards 0



    Ex: tokens = ["4","13","5","/","+"]
        output = 6

        When we hit "/"
        our previous two values are 13 and 5
            13 / 5 = 2

        Our array becomes
            ["4", "2", "+"]

        When we hit "+"
        our previous two values are 4 and 2
            4 + 2 = 6

        return 6
"""


"""
We'll use a stack 
We can push values onto our stack 
And whenever we reach an operator 
We'll pop the previous 2 values from our stack 

We'll perform the operation on the popped 2 values 
And push the result 
on the top of our stack 

When we pop,
we can use variables a,b 
to denote the previous 1 value 
and previous 2 value 
    *   this is needed b/c 
        order matters for 
        subtraction and division 
        
"""


class Solution(object):
    def evalRPN(self, tokens):
        stack = []

        for char in tokens:
            if char == "+":
                a, b = stack.pop(), stack.pop()
                stack.append(a + b)

            # order matters for subtraction
            elif char == "-":
                a, b = stack.pop(), stack.pop()
                stack.append(b - a)

            elif char == "*":
                a, b = stack.pop(), stack.pop()
                stack.append(a * b)

            # order matters for division
            elif char == "/":
                a, b = stack.pop(), stack.pop()
                stack.append(int(b / a))

            # append numbers
            else:
                stack.append(int(char))

        return stack[0]



if __name__ == '__main__':

    tokens = ["2","1","+","3","*"]
    tokens2 = ["4","13","5","/","+"]

    print(Solution().evalRPN(tokens))
    print(Solution().evalRPN(tokens2))

