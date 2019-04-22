#!/usr/bin/python3


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
    def lca(self, root, u, v):
        if root is None:
            return

        if root.val > u and root.val > v:
            return self.lca(root.left, u, v)

        if root.val < u and root.val < v:
            return self.lca(root.right, u, v)

        return root.val


if __name__ == '__main__':
    for _ in range(int(input())):
        N, Q = map(int, input().split())
        arr = list(map(int, input().split()))
        root = TreeNode(arr[0])
        for i in range(1, N):
            root = insertBST(root, arr[i])
        for _ in range(Q):
            u, v = map(int, input().split())
            print(Solution().lca(root, u, v), end=" ")
        print()
