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
    def inorderTraversal(self, root):
        if root is None:
            return

        self.inorderTraversal(root.left)
        print(root.val, end=" ")
        self.inorderTraversal(root.right)

    def preorderTraversal(self, root):
        if root is None:
            return

        print(root.val, end=" ")
        self.preorderTraversal(root.left)
        self.preorderTraversal(root.right)

    def postorderTraversal(self, root):
        if root is None:
            return

        self.postorderTraversal(root.left)
        self.postorderTraversal(root.right)
        print(root.val, end=" ")


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

    print("InorderTraversal: ")
    Solution().inorderTraversal(root)
    print("\nPreorderTraversal: ")
    Solution().preorderTraversal(root)
    print("\nPostorderTraversal: ")
    Solution().postorderTraversal(root)
    print()
