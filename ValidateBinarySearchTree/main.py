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
We can solve this using a recursive DFS 

For each node, 
we want to check if 
left < node < right

we'll be passing in left, right in our recursive function 

Our base case:
if not node
return True 
bc an empty node can be considered a good bst 

we'll do recursive calls on the nodes
left and right children 

In our recursive call to children 
we pass in 
node.left - for node.left, we know node.val is to the right.
            as such, node.left < node.val 
            In our dfs we say (left < node.val < right) 
            - in this scenario, we'd want to pass in 
            dfs(node, left, node.val)
            so that the above can hold true 
            
node.right - similarly we want 
             node.right > node.val 
             so we pass in dfs(node.right, node.val, right)
             such that right < node.val < left
             ie. the parent node's val would be passed in to the right position 

return true if if recursive calls for left, right child hold true 
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




