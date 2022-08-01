"""
450. Delete Node in a BST
"""

from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if root is None:
            return root

        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        else:
            # leaf node
            if not root.left and not root.right:
                return None
            # one child
            elif (not root.left and root.right) or (not root.right and root.left):
                if root.left:
                    return root.left
                else:
                    return root.right
            # two child
            else:
                temp = self.findMax(root.left)
                root.val = temp
                root.left = self.deleteNode(root.left, temp)
        return root

    def findMax(self, root):
        while root.right:
            root = root.right
        return root.val
        