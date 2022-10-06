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
We can solve this problem using a que 

We'll want to initialize a res = [] 
we will be appending [] to our res for each level 

Were also going to be using a que 

We will be going through the tree, 
adding vals to the que 

as we add values to the que we also want to len(q) values 
and append them to a list = []

We append list to our res 
return res 

"""

class Solution(object):
    def levelOrder(self, root):
        res = []

        que = collections.deque()

        # we start appending our root to our que
        que.append(root)

        while que:
            # qLen tells us how many times we'll be popping from our que
            qLen = len(que)

            # initialize variable for levels
            # we will be popping from our q for each level
            # and appending to levels

            level = []

            for i in range(qLen):
                # pop node from que
                # we will be appending node to levels
                node = que.popleft()

                # we also append the children to our que
                if node:
                    # append node to level
                    level.append(node.val)
                    que.append(node.left)
                    que.append(node.right)

            # append levels to res
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
