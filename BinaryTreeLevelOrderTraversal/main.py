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
We are given the root of a binary tree 
We want to return ans = [[]]

We are going to be traversing the tree 
level by level        
For each level, we want to append to a list 
and append list to ans 
return ans 

We can traverse the tree level by level 
using a que 

we'll append the root to our que 

while que:
we'll get queLen 
and initialize level 

for i in range q len, 
we want to append the nodes children to the que 

and we also want to pop nodes in our que 

this way, 
we are continuously adding nodes to our que 
corresponding to each level 

and when we pop from our que, we want to append 
to levels=[]

and append levels to ans 

"""

class Solution(object):
    def levelOrder(self, root):
        # initialize ans
        ans = []

        que = collections.deque()

        que.append(root)

        while que:
            levels = []

            # queLen
            queLen = len(que)

            for i in range(queLen):
                node = que.popleft()

                if node:
                    levels.append(node.val)
                    que.append(node.left)
                    que.append(node.right)

            if levels:
                ans.append(levels)

        return ans


if __name__ == '__main__':
    binary_tree = Tree()
    binary_tree.root = TreeNode(3)

    binary_tree.root.left = TreeNode(9)
    binary_tree.root.right = TreeNode(20)

    binary_tree.root.right.left = TreeNode(15)
    binary_tree.root.right.right = TreeNode(7)

    print(Solution().levelOrder(binary_tree.root))
