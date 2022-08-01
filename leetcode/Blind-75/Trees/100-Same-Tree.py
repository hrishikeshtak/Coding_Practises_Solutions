"""
100. Same Tree
"""

from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        elif p and q and p.val == q.val:
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        else:
            return False


p = TreeNode(3)
p.left = TreeNode(9)
p.right = TreeNode(20)
p.right.left = TreeNode(15)
p.right.right = TreeNode(7)

q = TreeNode(3)
q.left = TreeNode(9)
q.right = TreeNode(20)
q.right.left = TreeNode(15)
q.right.right = TreeNode(7)

print(f"isSameTree: {Solution().isSameTree(p, q)}")
