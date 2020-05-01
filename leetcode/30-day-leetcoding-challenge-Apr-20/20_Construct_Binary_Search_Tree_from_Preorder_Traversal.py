#!/usr/bin/python3

"""
Construct Binary Search Tree from Preorder Traversal
"""

from copy import deepcopy


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def bstFromPreorder(self, preorder: 'List[int]') -> 'TreeNode':

        if not preorder:
            return None

        # inorder for bst is sorted preorder
        inorder = deepcopy(preorder)
        inorder.sort()

        root = None

        root = self.insert(root, preorder, inorder)

        # return self.level_order_traversal(root)
        return root

    def insert(self, root, preorder, inorder):
        if not preorder or not inorder:
            return None

        val = preorder.pop(0)
        root = TreeNode(val)
        index = inorder.index(val)

        root.left = self.insert(root.left, preorder, inorder[:index])
        root.right = self.insert(root.right, preorder, inorder[index+1:])

        return root

    def level_order_traversal(self, root):
        if not root:
            return None
        queue = []
        queue.append(root)
        output = []

        while queue:
            temp = queue.pop(0)
            if temp:
                output.append(temp.val)
                if temp.left:
                    queue.append(temp.left)
                if temp.right:
                    queue.append(temp.right)

        return output


if __name__ == '__main__':
    preorder = [8, 5, 1, 7, 10, 12]
    # preorder = [10, 5, 1, 7, 40, 50]
    print(f"{Solution().bstFromPreorder(preorder)}")
