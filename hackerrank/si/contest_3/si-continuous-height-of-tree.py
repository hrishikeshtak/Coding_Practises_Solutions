#!/usr/bin/python3


class TreeNode:
    def __init__(self, K, level=0):
        self.val = K
        self.level = level
        self.left = None
        self.right = None


def insert(root, X, level, max_height):
    if root is None:
        max_height[0] = max(level, max_height[0])
        # print(X, level, max_height)
        return TreeNode(X, level)

    if X < root.val:
        root.left = insert(root.left, X, root.level+1, max_height)
    else:
        root.right = insert(root.right, X, root.level+1, max_height)
    return root


if __name__ == '__main__':
    for _ in range(int(input())):
        N = int(input())
        arr = list(map(int, input().split()))

        # insert in BST
        max_height = [0]
        root = None
        level = 0
        for i in range(0, N):
            root = insert(root, arr[i], level, max_height)
            print(max_height[0], end=" ")
        print()
