"""
104. Maximum Depth of Binary Tree
"""

from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Recursive
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))


# Iterative DFS
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0

        stack = [[root, 1]]
        res = 0

        while stack:
            node, depth = stack.pop()
            res = max(res, depth)
            if node.left:
                stack.append([node.left, depth+1])
            if node.right:
                stack.append([node.right, depth+1])
        return res


# Iterative BFS
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        
        q = [root]
        q.append(None)
        res = 1
        
        while len(q) > 1:
            node = q.pop(0)
            if node:
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            else:
                q.append(None)
                res += 1
        return res



root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)

print(f"maxDepth: {Solution().maxDepth(root)}")
