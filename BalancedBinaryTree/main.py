# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


class TreeNode(object):
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def dfs(root):
        if not root:
            return [True, 0]

        left = dfs(root.left)
        right = dfs(root.right)

        balanced = (left[0] and right[0] and
                    abs(left[1] - right[1]) <= 1)

        return [balanced, 1 + max(left[1], right[1])]

    return dfs(root)[0]



if __name__ == "__main__":
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)

    print(Solution().dfs(root))