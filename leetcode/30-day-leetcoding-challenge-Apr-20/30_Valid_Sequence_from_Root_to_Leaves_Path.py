#!/usr/bin/python3

"""
Check If a String Is a Valid Sequence from Root to Leaves Path in a Binary Tree
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidSequence(self, root: TreeNode, arr: 'List[int]') -> bool:
        return self.dfs(root, arr, len(arr), 0)

    def dfs(self, root, arr, n, index):
        if not root or index == n:
            return False

        if not root.left and not root.right:
            if root.val == arr[index] and index == n-1:
                return True
            return False

        return ((index < n) and (root.val == arr[index]) and \
                (self.dfs(root.left, arr, n, index+1) or \
                self.dfs(root.right, arr, n, index+1)))


if __name__ == '__main__':
    root = None
    root = TreeNode(0)
    root.left = TreeNode(1)
    root.left.left = TreeNode(0)
    root.left.right = TreeNode(1)
    root.left.left.right = TreeNode(1)
    root.left.right.left = TreeNode(0)
    root.left.right.right = TreeNode(0)
    root.right = TreeNode(0)
    root.right.left = TreeNode(0)

    print(f"{Solution().isValidSequence(root, [0, 1, 1, 0])}")
