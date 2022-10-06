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

        # we start at the root
        que.append(root)

        while que:
            # we want to get qLen
            qLen = len(que)

            level = []

            for i in range(qLen):
                # we pop from que
                node = que.popleft()

                # if node
                if node:
                    # we want to append the node to our level
                    level.append(node.val)

                    # and append the children to our que
                    que.append(node.left)
                    que.append(node.right)

            # if we have nodes in level,
            # we want to append to res
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
