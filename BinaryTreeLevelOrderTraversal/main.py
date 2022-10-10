import collections

from Trees import *

"""
Given the root
of a binary tree
return
the level order traversal 
of its nodes' values

ie from left to right 
level by level 

Ex:         3
           / \
         9    20
             /  \
           15    7
       
output: [3], [9, 20], [15, 7]

"""

"""
We want to return a list 
of nodes level x level 

We're going to be traversing the tree by level
breadth first search 

To implement, 
we'll use a que 

at each level we can add nodes to our que 

we'll also want to use a variable, levels = []
where we will be appending nodes in each level 

we'll pop nodes from the left of our que 
append to levels

and add the node's children into our que 

we'll do this for i in range (len(que))
which will run for the number of nodes 
in each level 

"""

class Solution(object):
    def levelOrder(self, root):
        # initialize ans
        ans = []

        que = collections.deque()

        que.append(root)

        while que:
            # get counter
            qLen = len(que)

            # initialize list to append node.val for each level
            level = []

            for i in range(qLen):
                # pop from que
                node = que.popleft()

                # if node
                if node:
                    level.append(node.val)

                    # append node's children
                    que.append(node.left)
                    que.append(node.right)

            # append levels to ans
            if level:
                ans.append(level)

        return ans


if __name__ == '__main__':
    binary_tree = Tree()
    binary_tree.root = TreeNode(3)

    binary_tree.root.left = TreeNode(9)
    binary_tree.root.right = TreeNode(20)

    binary_tree.root.right.left = TreeNode(15)
    binary_tree.root.right.right = TreeNode(7)

    print(Solution().levelOrder(binary_tree.root))
