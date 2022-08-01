"""
145. Binary Tree Postorder Traversal
"""

from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        if not root:
            return res
        stack = []
        cur = root
        stack.append(cur)
        while stack:
            cur = stack.pop()
            res.append(cur.val)
            if cur.left:
                stack.append(cur.left)
            if cur.right:
                stack.append(cur.right)
        return res[::-1]


root = TreeNode(1)
root.right = TreeNode(2)
root.right.left = TreeNode(3)

print(f"Tree Postorder Traversal: {Solution().postorderTraversal(root)}")

        