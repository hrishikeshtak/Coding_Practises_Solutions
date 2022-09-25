"""
112. Path Sum
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        
        def dfs(root, curSum):
            if not root:
                return False
            curSum += root.val
            if not root.left and not root.right: # Leaf node
                return curSum == targetSum
            return dfs(root.left, curSum) or dfs(root.right, curSum)
        return dfs(root, 0)
