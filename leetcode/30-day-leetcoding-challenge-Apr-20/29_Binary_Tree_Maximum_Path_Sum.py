#!/usr/bin/python3

"""
Binary Tree Maximum Path Sum

For this problem, a path is defined as any sequence of nodes from some
starting node to any node in the tree along the parent-child connections.
The path must contain at least one node and does not need to go through the root.
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def __init__(self):
        self.max_path_sum = -(1 << 31)

    def maxPathSum(self, root: TreeNode) -> int:
        max_sum = self.pathSum(root)
        return max(self.max_path_sum, max_sum)

    def pathSum(self, node):
        if node is None:
            return 0

        left = max(self.pathSum(node.left), 0)
        right = max(self.pathSum(node.right), 0)

        self.max_path_sum = max(self.max_path_sum, left + right + node.val)
        return max(left, right) + node.val


if __name__ == '__main__':
    # root = None
    # root = TreeNode(1)
    # root.left = TreeNode(2)
    # root.right = TreeNode(3)

    # root = None
    # root = TreeNode(-10)
    # root.left = TreeNode(9)
    # root.right = TreeNode(20)
    # root.right.left = TreeNode(15)
    # root.right.right = TreeNode(7)

    # root = None
    # root = TreeNode(-3)

    # root = None
    # root = TreeNode(2)
    # root.left = TreeNode(-1)

    root = None
    root = TreeNode(5)
    root.left = TreeNode(4)
    root.right = TreeNode(8)
    root.left.left = TreeNode(11)
    root.left.left.left = TreeNode(7)
    root.left.left.right = TreeNode(2)
    root.right.left = TreeNode(13)
    root.right.right = TreeNode(4)
    root.right.right.right = TreeNode(1)
    print(f"maxPathSum: {Solution().maxPathSum(root)}")
