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


def depth(root, key):
    if root is None:
        return

    if root.val == key:
        return 0

    if root.val < key:
        return 1 + depth(root.right, key)
    return 1 + depth(root.left, key)


if __name__ == '__main__':
    for _ in range(int(input())):
        N = int(input())
        arr = list(map(int, input().split()))
        root = TreeNode(arr[0])
        for i in range(1, N):
            root = insertBST(root, arr[i])
        for i in range(0, N):
            print(depth(root, arr[i]), end=" ")
        print()
