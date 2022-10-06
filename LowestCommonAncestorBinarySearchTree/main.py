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
To solve this problem 
we can start evaluating at the root
since the root is a common ancestor 
of ALL the nodes within the tree 

In a Binary Search Tree
the left subtree of a node, contains nodes with smaller values 
the right subtree of a node contains keys with greater values 
Ex:             8
              /   \
            3      10
           / \       \
         1    6       14
             / \      /
            4   7     13
            
The lowest common ancestor of two nodes, p & q
occurs at the point where p & q split into separate trees 

ie. in the tree above, 
the LCA between nodes 1 & 6 = 3
the LCA between nodes 4 & 7 = 6
the LCA between nodes 1 & 7 = 3
the LCA between nodes 4 & 13 = 8

Bc nodes in a BST are increasing from left -> right 
if we are given two nodes whose values are greater than root.left
both nodes will be going pertain to the RIGHT tree 

Ex:              6
               /   \
              2      8
             / \    /  \
            0   4  7    9
                /\
               3  5

Nodes 7 and 9 are greater than root.left
Nodes 7 and 9 pertain to the same subtree
    bc both 7 and 9 pertain to the same subtree, 
    we dont need to search left!
    we can just search right subtree, 
    as both 7 & 9 pertain only to the right subtree, NOT left 

ie We are looking for the split between two nodes! 


*** in this problem, 
if we are ever passed the root node as one of our inputs, 
the LCA between inputs will always be the root node!  
ie the root cannot be a child of any other node but itself! 
"""

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        # pointer to root node
        current = root

        while current:
            # if both p & q > current.val
            if p.val > current.val and q.val > current.val:
                # we only need to search RIGHT
                current = current.right

            # if both p & q < current.val
            elif p.val > current.val and q.val > current.val:
                # we only need to search LEFT
                current = current.left

            # if p & q do not move in the same direction
            # we have a split! ie we've found LCA
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




