from Trees import *

"""
Given the root of a binary tree
determine if it is a valid binary search tree

A valid BST is defined as
-   every node in the left subtree is less than root 

-   every node in the right subtree is greater than root 

-   left and right subtree must also be BST


"""

"""
To solve, 
we'll be doing this recursively 

we'll set up our recursive function 
and pass in node, leftBoundary, rightBoundary
def dfs(node):

for our base case
we'll say if not node:
return True 

for a node to be valid, 
it must be 
left < node.val < right

if not (left < node.val < right)
return False 


we'll update left, right boundaries 
on each recursive call

node.left must be smaller than node
as such, we'll pass node.val as the right boundary 
dfs(node.left, left, node.val)

node.right must be larger than node 
as such, we'll pass node.val as the left boundary 
dfs(node.right, node.val, right)

we'll return    (dfs(node.left, left, node.val) and 
                dfs(node.right, node.val, right))
                
to initialize the recursive call 
we return dfs(root, float(-inf), float(inf))
                
"""

class Solution(object):
    def isValidBST(self, root):

        # recursive function
        def dfs(node, left, right):

            # base case
            if not node:
                return True

            # if not true, we want to return False
            if not (left < node.val < right):
                return False

            # recursive call to children
            return dfs(node.left, left, node.val) and \
                   dfs(node.right, node.val, right)

        # return ans
        return dfs(root, float("-inf"), float("inf"))


if __name__ == '__main__':
    tree = Tree()

    tree.root = TreeNode(2)

    tree.root.left = TreeNode(1)
    tree.root.right = TreeNode(3)

    print(Solution().isValidBST(tree.root))




