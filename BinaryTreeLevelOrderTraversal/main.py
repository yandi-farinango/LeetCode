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
Looking at the output 
we can see that we want to essentially return 
a list of nodes for each level 

We are going to be traversing the tree
from left -> right 
one level at a time 


We want to run BFS!! 


We'll be using a que 



"""

class Solution(object):
    def levelOrder(self, root):
        # initialize res
        res = []

        # initialize que
        q = collections.deque()
        q.append(root)

        while q:
            # get the number of elements in our q
            # we will be removing qLen elements from our q
            qLen = len(q)

            level = []

            for i in range(qLen):
                # we pop from q
                node = q.popleft()

                # and add its children to our q
                if node:
                    level.append(node.val)
                    q.append(node.left)
                    q.append(node.right)

            if level:
                res.append(level)

        return res

if __name__ == '__main__':
    binary_tree = Tree()
    binary_tree.root = TreeNode(3)

    binary_tree.root.left = TreeNode(9)
    binary_tree.root.right = TreeNode(20)

    binary_tree.root.right.left = TreeNode(15)
    binary_tree.root.right.right = TreeNode(7)

    print(Solution().levelOrder(binary_tree.root))
