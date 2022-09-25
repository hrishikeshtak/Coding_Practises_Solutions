"""
101. Symmetric Tree
"""

from collections import deque
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        def isMirrorRecursive(left, right):
            if left is None and right is None:
                return True
            if left is None or right is None:
                return False
            else:
                return left.val == right.val and \
                       isMirrorRecursive(left.left, right.right) and \
                       isMirrorRecursive(left.right, right.left)
        return isMirrorRecursive(root, root)

    def isSymmetricIterative(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        q = deque([root.left, root.right])
        while q:
            left, right = q.popleft(), q.pop()
            if not left and not right:
                continue
            if not left or not right:
                return False
            if left.val != right.val:
                return False
            q.appendleft(left.left)
            q.append(right.right)
            q.appendleft(left.right)
            q.append(right.left)
        return True
