"""
Design a stack that supports
push, pop, top, and
retrieving the minimum element in constant time.
"""

"""
The tricky thing here is being able to 
return the min value in our stack 
in constant time 

To do this 
We'll actually use 2 separate stacks 

stack1
will hold values we've added 
in the order that we add to our stack 

stack2 will hold the minValue 
as we continuously add 
to our stack 

adding and popping 
operating will be done on both stacks 

peek operation 
will be done only on s1

getMin operation 
will be done on s2
"""

class MinStack:
    def __init__(self):
        self.stack = []
        self.minStack = []


    def push(self, val: int) -> None:
        self.stack.append(val)

        # for our minStack
        # since our minStack
        # is essentially a stack of min vals
        # we want to push the min val

        # to do this we'll update val
        # to be min of val and
        # the value currently at the top of our minStack
        val = min(val, self.minStack[-1] if self.minStack else val)
        self.minStack.append(val)

    def pop(self) -> None:
        # we pop from both stacks
        self.stack.pop()
        self.minStack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minStack[-1]





if __name__ == '__main__':
    obj = MinStack()
    obj.push(-2)
    obj.push(0)
    obj.push(-3)
    print(obj.getMin())     # return -3
    obj.pop()
    print(obj.top())        # return 0
    print(obj.getMin())     # return -2

