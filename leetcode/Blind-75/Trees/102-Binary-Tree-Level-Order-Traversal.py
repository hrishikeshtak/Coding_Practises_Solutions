"""
102. Binary Tree Level Order Traversal
"""

from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        if not root:
            return res
        q = []
        cur = root
        q.append(cur)
        q.append(None)
        temp = []
        while len(q) > 1:
            cur = q.pop(0)
            if cur:
                temp.append(cur.val)
                if cur.left:
                    q.append(cur.left)
                if cur.right:
                    q.append(cur.right)
            else:
                res.append(temp)
                temp = []
                q.append(None)
        if temp:
            res.append(temp)
        return res


root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)

print(f"Tree levelOrder Traversal: {Solution().levelOrder(root)}")
