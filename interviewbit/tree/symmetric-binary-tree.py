#!/usr/bin/python3


# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # @param A : root node of tree
    # @return an integer
    def isSymmetric(self, A):
        return self.isMirror(A, A)

    def isMirror(self, A, B):
        if A is None and B is None:
            return 1
        elif A is None:
            return 0
        elif B is None:
            return 0

        if A.val == B.val:
            return self.isMirror(A.left, B.right) and \
                self.isMirror(A.right, B.left)
        else:
            return 0


if __name__ == '__main__':
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(2)
    root.left.left = TreeNode(3)
    root.right.right = TreeNode(3)
    root.left.right = TreeNode(4)
    root.right.left = TreeNode(4)
    print(Solution().isSymmetric(root))
