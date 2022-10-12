from Trees import *

"""
Given the root of a BST, 
and an integer K 
return the kth smallest value 
of all the values of the nodes in the tree

    Ex:     3
           /  \
          1    4
           \
            2

        k = 2
        return 2
        
        ie 2 is the 2nd smallest element in the BST 
        
"""

"""
To do this
we want to search the tree according to the node values 

We can do this using a stack 

We know that in a BST the smallest values are going to be the leftmost
we want to shift our pointer in the leftmost direction 

We want to be appending/popping values from our stack in value order 
we'll use a counter that will get incremented whenever we pop 
this will keep track of when we've found the nth smallest value 

First we want to be appending the leftmost values 
we can append current 
and reset current = current.left 

we'll pop from our stack 
and have current = pop
we increment our counter 

if counter == k 
return current .val

now we set current = current.right 
such that the current.right resets the loop
and gets appended to our stack on the reset 
"""

class Solution(object):
    def kthSmallest(self, root, k):
        # counter
        n = 0

        stack = []

        current = root

        while current or stack:
            while current:
                # appending leftmost values
                stack.append(current)
                current = current.left

            current = stack.pop()

            # increment counter
            n += 1

            if n == k:
                return current.val

            # set current = current.right
            # such that it resents the loop
            # current.right gets appended to our stack at reset
            current = current.right


if __name__ == '__main__':
    tree = Tree()
    tree.root = TreeNode(5)

    tree.root.left = TreeNode(3)
    tree.root.right = TreeNode(6)

    tree.root.left.left = TreeNode(2)
    tree.root.left.right = TreeNode(4)

    tree.root.left.left.left = TreeNode(1)

    print(Solution().kthSmallest(tree.root, 4))