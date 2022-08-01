"""
94. Binary Tree Inorder Traversal
"""

from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return root
        stack = []
        cur = root
        res = []
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


root = TreeNode(1)
root.right = TreeNode(2)
root.right.left = TreeNode(3)

print(f"Tree Inorder Traversal: {Solution().inorderTraversal(root)}")
