#!/usr/bin/python3


# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # @param A : root node of tree
    # @return a list of integers
    def preorderTraversalRecursive(self, root):
        if root is None:
            return

        print(root.val, end=" ")
        self.preorderTraversalRecursive(root.left)
        self.preorderTraversalRecursive(root.right)

    def preorderTraversal(self, root):
        stack = []
        res = []
        cur = root

        stack.append(cur)

        while stack:
            cur = stack.pop()
            res.append(cur.val)
            if cur.right:
                stack.append(cur.right)
            if cur.left:
                stack.append(cur.left)
        return res


if __name__ == '__main__':
    root = None
    root = TreeNode(5)
    root.left = TreeNode(10)
    root.left.right = TreeNode(2)
    root.left.right.left = TreeNode(-1)
    root.left.right.right = TreeNode(12)
    root.right = TreeNode(-3)
    root.right.left = TreeNode(7)
    root.right.right = TreeNode(6)
    root.right.right.left = TreeNode(1)
    root.right.right.right = TreeNode(8)

    print("preorderTraversalRecursive: ")
    Solution().preorderTraversalRecursive(root)
    print("\npreorderTraversalIterative: ")
    print(Solution().preorderTraversal(root))
    print()
