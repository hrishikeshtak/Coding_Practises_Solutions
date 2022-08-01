"""
199. Binary Tree Right Side View
"""

from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        res = []
        q = []
        q.append(root)
        q.append(None)

        cur = root
        cnt = 0. # to count the nodes
        while len(q) > 1:
            cur = q.pop(0)
            cnt += 1
            if cur:
                if cnt == 1:
                    res.append(cur.val)
                if cur.right:
                    q.append(cur.right)
                if cur.left:
                    q.append(cur.left)
            else:  # None
                cnt = 0  # before next level starts, reset cnt
                q.append(None)
        return res
