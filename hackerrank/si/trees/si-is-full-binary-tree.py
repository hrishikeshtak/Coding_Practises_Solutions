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


def isFullBT(root):
    if root is None:
        return True

    if root.left is None and root.right is None:
        return True
    if root.left and root.right is None:
        return False
    elif root.right and root.left is None:
        return False

    return isFullBT(root.left) and isFullBT(root.right)


if __name__ == '__main__':
    for _ in range(int(input())):
        N = int(input())
        arr = list(map(int, input().split()))
        root = TreeNode(arr[0])
        for i in range(1, N):
            root = insertBST(root, arr[i])
        status = isFullBT(root)
        if status:
            print("True")
        else:
            print("False")
