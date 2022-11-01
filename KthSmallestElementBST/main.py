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

we'll have a variable current = root 

while current or stack 
    while current 
        append left values to our stack 
        shift current pointer to get leftmost values 
        current = current.left 

current = stack.pop()

we'll increment our counter 

if counter == k:
return current.val 

shift current pointer = current.right 

this resets our while loop 
such that the right child 
is then appended to our stack 
in value order 
            
"""

class Solution(object):
    def kthSmallest(self, root, k):
        counter = 0

        stack = []

        current = root

        while current or stack:
            while current:
                # append current
                stack.append(current)

                # shift current left
                current = current.left

            current = stack.pop()

            counter += 1

            if counter == k:
                return current.val

                # shift pointer right
            current = current.right


if __name__ == '__main__':
    tree = Tree()
    tree.root = TreeNode(5)

    tree.root.left = TreeNode(3)
    tree.root.right = TreeNode(6)

    tree.root.left.left = TreeNode(2)
    tree.root.left.right = TreeNode(4)

    tree.root.left.left.left = TreeNode(1)

    print(Solution().kthSmallest(tree.root, k=3))