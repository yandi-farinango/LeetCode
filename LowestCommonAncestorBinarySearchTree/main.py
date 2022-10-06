from Trees import *

"""
Given a binary search tree
find the lowest common ancestor (LCA)
of two given nodes

The LCA between two nodes, p & q
is defined as
the lowest node, T,
that has both p & q as descendants
    * a node may be a descendant of itself

"""

"""
In a binary search tree, 
we can see that the lowest common ancestor between two nodes 
occurs when the nodes split off into different trees 

            Ex:
            6
           / \
         2     8
       /  \   /  \
      0    4 7    9
          /\
         3  5

    - The LCA between two nodes 3 and 5 occurs at node 4,
    where 3 and 5 split into separate trees 
    
    - The LCA between two nodes 4 and 9 occurs at node 6 
    where nodes 4 and 9 split into separate trees 

Knowing this, 

To solve this problem we can, 
start at the root node, 
and evaluate where p and q both move in the same direction 
We can see that 
    -   if both nodes > current.left 
        both nodes are in teh RIGHT tree
    
    -   if both nodes < current.right 
        both nodes are in the LEFT tree
        
    -   else there is a split! 
        return the node where the split occurs 
"""

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        # pointer to root
        current = root

        while current:
            # both p and q are greater than current
            if p.val > current.val and q.val > current.val:
                # search RIGHT
                current = current.right

            # both p and q are less than current
            elif p.val < current.val and q.val < current.val:
                # serach LEFT
                current = current.left

                # We've found the split!
            else:
                return current


if __name__ == '__main__':
    bst = Tree()
    bst.root = TreeNode(6)

    # node P
    bst.root.left = TreeNode(2)

    # node Q
    bst.root.right = TreeNode(8)

    bst.root.left.left = TreeNode(0)
    bst.root.left.right = TreeNode(4)

    bst.root.right.left = TreeNode(7)
    bst.root.right.right = TreeNode(9)

    bst.root.left.right.left = TreeNode(3)
    bst.root.left.right.right = TreeNode(5)

    LCA = Solution().lowestCommonAncestor(bst.root, bst.root.left, bst.root.right)
    print(LCA.val)




