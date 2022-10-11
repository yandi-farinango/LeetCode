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
For this problem
we want to perform a value order traversal 

We know that the smallest values are going to be the left most children 

We can use a stack 
and append the left most nodes 

We'll want to use a counter n 
which will be updated continuously

we'll set our current pointer to root 

while current or stack 
while current 
    we want to append the current value to our stack 
    and set current= current.left; ie we want to move in the leftmost direction
    
we'll pop from our stack, 
our current value would now be the left most val
current = stack.pop
and we'll update the counter 

if counter == K 
return current.val

and we append current's right child 

this way we are appending values in value-order 
and when n == k 
we've found the nth smallest val
"""

class Solution(object):
    def kthSmallest(self, root, k):
        # counter
        n = 0

        stack = []

        current = root

        while current or stack:
            while current:
                # append current
                stack.append(current)
                # shift current towards the leftmost direction
                current = current.left

            # pop
            current = stack.pop()

            # increment counter
            n += 1

            if n == k:
                return current.val

            # set current = current.right
            # such that it will reset the loop
            # current.right get appended to our stack in the loop reset
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