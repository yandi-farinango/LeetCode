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
We can see from the given arrays 
That we can solve this problem recursively 

basecase 
if not preorder or not inorder return None


The root node is always found at preorder[0]


To create the subtrees, we need to know where to partition 
the inorder array 

We'll need to get the index of the root within our inorder array
mid = inorder.index(preorder[0])


To build the tree recursively, 
we pass in 


root.left = self.buildTree()
      
    For passing in preorder, 
    We want the next root node; ie root.left 
    to be found at the 0th index of preorder 
    and we want pass in all the nodes that will be in the left subtree 
    this partition is found at 
    preorder[1: mid + 1]


    for passing in inorder, 
    we want all the values that correspond to the left subtree 
    ie, the values up to mid 
    this partition is found at 
    inorder[:mid]
    

root.right = self.buildTree()

    for passing in preorder, 
    we want the next root node; ie root.right 
    to be found at the 0th index of preorder 
    and we want to pass in all the nodes that will be in the right subtree
    this partition is found at 
    preorder[mid+1:]
    
    
    for passing in inorder
    we want all the values that correspond to the right subtree
    ie the values after mid 
    this partition is found at 
    inorder[mid+1:]
"""


class Solution(object):
    def buildTree(self, preorder, inorder):
        # base case
        if not preorder or not inorder:
            return None

            # construct root
        root = TreeNode(preorder[0])

        # get index
        mid = inorder.index(preorder[0])

        # recursive calls for constructing subtrees
        root.left = self.buildTree(preorder[1:mid + 1], inorder[:mid])
        root.right = self.buildTree(preorder[mid + 1:], inorder[mid + 1:])

        return root


if __name__ == '__main__':
    preorder = [1, 2, 4, 5, 3, 6, 7]
    inorder = [4, 2, 5, 1, 6, 3, 7]

    ans = Solution().buildTree(preorder, inorder)

    print(ans)
