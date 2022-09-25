"""
230. Kth Smallest Element in a BST
Given the root of a binary search tree, and an integer k, return the kth smallest value (1-indexed)
of all the values of the nodes in the tree.
"""

from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack = []
        cur = root
        while cur or stack:
            while cur:
                stack.append(cur)
                cur = cur.left
            cur = stack.pop()
            k -= 1
            if k == 0:
                return cur.val
            cur = cur.right

    # using inorderTraversal
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        inorder = self.inorderTraversal(root)
        # print(f"inorder: {inorder}")
        return inorder[k-1]

    def inorderTraversal(self, root):
        stack = []
        res = []
        cur = root
        while True:
            if cur:
                stack.append(cur)
                cur = cur.left
            else:
                if stack:
                    cur = stack.pop()
                    res.append(cur.val)
                    cur = cur.right
                else:
                    break
        return res
