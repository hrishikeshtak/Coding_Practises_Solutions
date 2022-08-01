"""
105. Construct Binary Tree from Preorder and Inorder Traversal
"""

from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None

        root = TreeNode(preorder[0])
        mid = inorder.index(preorder[0])
        root.left = self.buildTree(preorder[1:mid+1], inorder[:mid])
        root.right = self.buildTree(preorder[mid+1:], inorder[mid+1:])
        return root


def PostorderTraversalIterative(root: Optional[TreeNode]) -> List[int]:
    if not root:
        return []

    stack = []
    res = []

    stack.append(root)
    while stack:
        cur = stack.pop()
        res.append(cur.val)
        if cur.left:
            stack.append(cur.left)
        if cur.right:
            stack.append(cur.right)
    return res[::-1]


root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)

preorder = [3,9,20,15,7]
inorder = [9,3,15,20,7]
root = Solution().buildTree(preorder, inorder)
print(f"Preorder Traversal: {preorder}")
print(f"Inorder Traversal: {inorder}")
print(f"Postorder Traversal Iterative: {PostorderTraversalIterative(root)}")
