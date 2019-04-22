#!/usr/bin/python3

"""
Given a binary tree containing digits from 0-9 only, each root-to-leaf path
could represent a number.
An example is the root-to-leaf path 1->2->3 which represents the number 123.
Find the total sum of all root-to-leaf numbers % 1003.
"""

M = int(1e9 + 7)


# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def insertBST(root, key):
    if root is None:
        return TreeNode(key)
    if root.val < key:
        root.right = insertBST(root.right, key)
    else:
        root.left = insertBST(root.left, key)

    return root


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
            # print(s1)
            total += int(s1)

        return total % M


if __name__ == '__main__':
    for _ in range(int(input())):
        N = int(input())
        arr = list(map(int, input().split()))
        root = TreeNode(arr[0])
        for i in range(1, N):
            root = insertBST(root, arr[i])
        print(Solution().sumNumbers(root))
