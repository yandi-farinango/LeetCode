import collections

from Trees import *

"""
Given the root of a binary tree 
imagine yourself standing 
on the right side of it 
return the values of the nodes you'd see 
from top -> bottom 

    Ex:         1        <-
               / \
              2   3      <-
               \   \
                5   4    <-
                
        return [1,3,4]
    
"""

"""
We essentially want to return 
the right-most node for each level 

We're going to want to use Breadth-First-Search (Level-order-Traversal)

We can implement BFS using a que 

We can initially add the root node to our que 

We'll also initialize a res variable 

We can add the right-most value in our que 
to res 

we'll be popping nodes from our que 
and adding node's children as we move 
level by level 
"""

class Solution(object):
    def rightSideView(self, root):

        # initialize res and que
        res = []
        que = collections.deque()

        que.append(root)

        while que:
            # placeholder for rightSide
            rightSide = None

            qLen = len(que)

            # for nodes in each level
            for i in range(qLen):
                node = que.popleft()

                if node:
                    # update rightSide
                    rightSide = node

                    # append children
                    que.append(node.left)
                    que.append(node.right)

            # append rightSide
            if rightSide:
                res.append(rightSide.val)

        return res


if __name__ == '__main__':
    tree = Tree()

    tree.root = TreeNode(1)

    tree.root.left = TreeNode(2)
    tree.root.right = TreeNode(3)

    tree.root.left.right = TreeNode(5)

    tree.root.right.right = TreeNode(4)

    print(Solution().rightSideView(tree.root))

