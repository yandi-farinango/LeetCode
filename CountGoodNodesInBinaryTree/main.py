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
We're going to solve this recursively 
where we'll have a variable, res, 
that will get incremented 
at each recursive call 

we'll also be passing along maxVal 
which will get updated at each level 
ie res += 1 if node.val >= maxVal

To set up our recursive function, 
We can start with our base case 

if not node:
return 0 

we'll then set up our res counter
res = 1 if node.val >= maxVal

we update maxVal continuously at each recursive loop 

and 
increment res 
on the recursive calls 
ie  res += recursion(node.left, maxVal)
    res += recursion(node.right, maxVal)


"""

class Solution(object):
    def goodNodes(self, root):

        def recursion(node, maxVal):
            if not node:
                return 0

            # initialize res tracker
            res = 1 if node.val >= maxVal else 0

            # update maxVal
            maxVal = max(maxVal, node.val)

            # increment res on recursive calls
            res += recursion(node.left, maxVal)
            res += recursion(node.right, maxVal)

            return res

        # main recursive call
        return recursion(root, root.val)


if __name__ == '__main__':
    tree = Tree
    tree.root = TreeNode(3)

    tree.root.left = TreeNode(1)
    tree.root.right = TreeNode(4)

    tree.root.left.left = TreeNode(3)

    tree.root.right.left = TreeNode(1)
    tree.root.right.right = TreeNode(5)


    print(Solution().goodNodes(tree.root))
