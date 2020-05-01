#!/usr/bin/python3

"""
Diameter of Binary Tree
Given a binary tree, you need to compute the length of the diameter of
the tree. The diameter of a binary tree is the length of the longest
path between any two nodes in a tree.
This path may or may not pass through the root.
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0

        lheight = self.height(root.left)
        rheight = self.height(root.right)

        ldiameter = self.diameterOfBinaryTree(root.left)
        rdiameter = self.diameterOfBinaryTree(root.right)

        return max(lheight + rheight, max(ldiameter, rdiameter))

    def height(self, root):
        if root is None:
            return 0

        return max(self.height(root.left), self.height(root.right)) + 1


if __name__ == '__main__':
    root = None
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)

    print(f"Diameter = {Solution().diameterOfBinaryTree(root)}")
