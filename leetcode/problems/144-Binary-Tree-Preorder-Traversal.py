"""
144. Binary Tree Preorder Traversal
"""

from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        
        stack = []
        res = []
        cur = root
        stack.append(cur)
        
        while stack:
            cur = stack.pop()
            res.append(cur.val)
            
            if cur.right:
                stack.append(cur.right)
            if cur.left:
                stack.append(cur.left)
        return res


root = TreeNode(1)
root.right = TreeNode(2)
root.right.left = TreeNode(3)

print(f"Tree Preorder Traversal: {Solution().preorderTraversal(root)}")
