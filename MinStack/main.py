"""
Design a stack that supports
push, pop, top, and
retrieving the minimum element in constant time.
"""

"""
We need to design a stack that supports push, pop, top, 
and
retreiving min element in CONSTANT time 

To retreive the min element in CONSTANT time 
We want the min element to be easily accesible 

i.e at the top of a stack

So... 

We can use two stacks! 

stack 
and min stack 

Min stack will always have the minVal at the top of the stack 
i.e we'll push min(val, minStack[-1]) to our minStack 
"""


class MinStack:
    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        self.stack.append(val)
        self.minStack.append(min(val, self.minStack[-1]) if self.minStack else val)

    def pop(self):
        """
        :rtype: None
        """
        self.stack.pop()
        self.minStack.pop()

    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1]

    def getMin(self):
        """
        :rtype: int
        """
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

