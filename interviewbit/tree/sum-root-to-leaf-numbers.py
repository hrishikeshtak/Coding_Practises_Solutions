#!/usr/bin/python3

"""
Given a binary tree containing digits from 0-9 only, each root-to-leaf path
could represent a number.
An example is the root-to-leaf path 1->2->3 which represents the number 123.
Find the total sum of all root-to-leaf numbers % 1003.
"""


# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# Definition for a  binary tree node
# class TreeNode:
#    def __init__(self, x):
#        self.val = x
#        self.left = None
#        self.right = None

class Solution:
    # @param A : root node of tree
    # @return an integer
    def sumNumbers(self, root):
        results = []

        if not root:
            return 0

        def pathSumRec(root, path):
            if root is None:
                return 0

            path.append(root.val)

            if root.left is None and root.right is None:
                # print(path, sum(path))
                results.append(list(path))

            if root.left:
                pathSumRec(root.left, path)
            if root.right:
                pathSumRec(root.right, path)
            path.pop()

        pathSumRec(root, [])

        # print(results)
        total = 0
        for path in results:
            s1 = ""
            for i in path:
                s1 += str(i)
            total += int(s1)

        return total % 1003


if __name__ == '__main__':
    # root = TreeNode(5)
    # root.left = TreeNode(4)
    # root.right = TreeNode(8)
    # root.left.left = TreeNode(11)
    # root.right.left = TreeNode(13)
    # root.right.right = TreeNode(4)
    # root.left.left.left = TreeNode(7)
    # root.left.left.right = TreeNode(2)
    # root.right.right.left = TreeNode(5)
    # root.right.right.right = TreeNode(1)

    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    print(Solution().sumNumbers(root))
