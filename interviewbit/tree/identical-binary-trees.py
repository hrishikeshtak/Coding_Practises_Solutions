#!/usr/bin/python3


# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # @param A : root node of tree
    # @param B : root node of tree
    # @return an integer
    def isSameTree(self, A, B):
        if A is None and B is None:
            return 1
        elif A is None:
            return 0
        elif B is None:
            return 0

        if A.val == B.val:
            return self.isSameTree(A.left, B.left) and \
                self.isSameTree(A.right, B.right)
        else:
            return 0


if __name__ == '__main__':
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(4)

    root1 = TreeNode(1)
    root1.left = TreeNode(2)
    root1.right = TreeNode(3)

    print(Solution().isSameTree(root, root1))
