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


def countNodes(root):
    if root is None:
        return 0

    return 1 + countNodes(root.left) + countNodes(root.right)


def isCompleteBT(root, index, N):
    if root is None:
        return True

    if index >= N:
        return False

    return isCompleteBT(root.left, 2*index+1, N) and isCompleteBT(
        root.right, 2*index+2, N)


if __name__ == '__main__':
    for _ in range(int(input())):
        N = int(input())
        arr = list(map(int, input().split()))
        root = TreeNode(arr[0])
        for i in range(1, N):
            root = insertBST(root, arr[i])
        N = countNodes(root)
        # print("Total Nodes: ", N)
        status = isCompleteBT(root, 0, N)
        if status:
            print("Yes")
        else:
            print("No")
