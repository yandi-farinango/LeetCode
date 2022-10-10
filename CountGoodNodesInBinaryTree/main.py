from Trees import *

"""
Given a binary tree root
a node, X,
is named good
if, in the path from root -> x
there are no nodes with values greater than x

return the number of good nodes
in the binary tree

    Ex:
                    3
                  /   \
                1      4
              /      /  \
            3       3    5

        return 4
        ie root node is always good
        nodes 3->4->5 are good
        node 1 is not GOOD; 3 is greater than 1 on path 3->1
        node 3 is good; no nodes are greater on path 3->1->3

"""

"""
We can solve this recursively 
depth first search

We'll set up our recursive function: 
For each node, we want to check 
if any prior node's value is greater 
we'll be passing maxVal in our recursive dfs 

Our base case - if not node:
return 0 bc an empty tree wont have any good nodes 

res = 1 if node.val >= maxVal else 0 
update maxVal

increment res on recursive dfs call to left and right subtree 
return res 

After we've set up the recursive function, 
we can pass dfs(root, root.val) 
"""

class Solution(object):
    def goodNodes(self, root):
        # set up recursive dfs
        def dfs(node, maxVal):
            # base case
            if not node:
                return 0

            # initialize variable for res
            res = 1 if node.val >= maxVal else 0

            # update maxVal
            maxVal = max(maxVal, node.val)

            # recursive call to subtrees
            res += dfs(node.left, maxVal)
            res += dfs(node.right, maxVal)

            return res

        return dfs(root, root.val)


if __name__ == '__main__':
    tree = Tree
    tree.root = TreeNode(3)

    tree.root.left = TreeNode(1)
    tree.root.right = TreeNode(4)

    tree.root.left.left = TreeNode(3)

    tree.root.right.left = TreeNode(1)
    tree.root.right.right = TreeNode(5)


    print(Solution().goodNodes(tree.root))
