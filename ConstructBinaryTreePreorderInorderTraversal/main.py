from Trees import *

"""
Given two integer arrays
pre-order, preorder traversal of a binary tree
in-order, inorder traversal of a binary tree

construct and return the binary tree

    Ex: preorder = [3,9,20,15,7]
        inorder = [9,3,15,20,7]

                3
              /  \
             9    20
                 /  \
                15   7

"""

"""
We need to know:
- First number in preorder traversal is always going to be the ROOT
- We can determine which subtree other values correspond to by looking at the inorder traversal 
- We can look for the ROOT val in our inorder traversal array 
- If we can identify the ROOT from our preorder traversal,
  we can see that, in our inorder traversal, numbers to the left of ROOT
  will correspond to the left subtree, same for right 
  

For our code, 
we are getting the first value in our preorder array, 
looking up that value in our inorder array 

from our inorder array, we can get a sense of what values are in the left, right subtrees

We know where to partition our preorder array; ie partition our tree; because 
the len of the values to the left 
and len of the values to the right 

We can do this recursively! 

# Creating the recursive function 
Base case:  if we don't have any nodes to traverse ie 
            if not preorder or not inorder
            :return null
            
we'll create our root node      * root is at position preorder[0]
root = TreeNode(preorder[0])

We want to find the position of our "root" in our inorder array
mid = inorder.index(preorder[0])


We can build our tree recursively
where we can pass in our partitioned preorder and inorder sub-arrays 

For left subtree, root.left, we want 
preorder - every node to the left of mid; we pass in: preorder[1: mid+1]
inorder - every node up until mid; we pass in inorder[:mid]

For right subtree, root.right, we want 
preorder - every node to the right of mid; we pass in: preorder[mid+1:]
inorder - every node to the right of mid; we pass in: inorder[mid + 1:]

return root 
"""


class Solution(object):
    def buildTree(self, preorder, inorder):
        # base case
        if not preorder or not inorder:
            return None

        # create root TreeNode; root found at position preorder[0]
        root = TreeNode(preorder[0])

        # find root position in inorder array
        mid = inorder.index(preorder[0])

        # we can build our subtrees recursively
        # we pass in our new preorder and inorder sub-arrays
        root.left = self.buildTree(preorder[1:mid + 1], inorder[:mid])
        root.right = self.buildTree(preorder[mid + 1:], inorder[mid + 1:])

        return root


if __name__ == '__main__':
    preorder = [3, 9, 20, 15, 7]
    inorder = [9, 3, 15, 20, 7]

    ans = Solution().buildTree(preorder, inorder)

    print(ans)
