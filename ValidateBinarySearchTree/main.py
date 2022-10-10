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
We can solve this problem 
using a recursive DFS

For our recursive function 
we're going to pass in the node 
and the left and right boundaries 


# base case
if not node 
return True 
bc an empty would be valid 



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




