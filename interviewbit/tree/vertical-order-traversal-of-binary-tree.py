#!/usr/bin/python3

from collections import defaultdict


# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # @param A : root node of tree
    # @return a list of list of integers
    def verticalOrderTraversal(self, root):
        # store horizontal distance of each node from root node
        m = defaultdict(list)

        # HD of root is 0
        m = self.verticalOrderTraversalUtil(root, 0, m)
        # print(m)

        res = []
        # sort m based on keys
        for key in sorted(m):
            # print(m[key])
            res.append(m[key])
        return res

    def verticalOrderTraversalUtil(self, root, level, m):
        # Pre Order based traversal
        if root is None:
            return m

        m[level].append(root.val)

        if root.left:
            self.verticalOrderTraversalUtil(root.left, level - 1, m)

        if root.right:
            self.verticalOrderTraversalUtil(root.right, level + 1, m)

        return m


if __name__ == '__main__':
    root = TreeNode(4)
    root.left = TreeNode(2)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(3)
    root.left.right.right = TreeNode(10)
    root.left.right.right.left = TreeNode(30)
    root.right = TreeNode(6)
    root.right.left = TreeNode(5)
    root.right.right = TreeNode(8)

    print(Solution().verticalOrderTraversal(root))
