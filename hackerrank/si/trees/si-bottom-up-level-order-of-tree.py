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


def height(root):
    if root is None:
        return -1

    return max(height(root.left), height(root.right)) + 1


def bottom_level_order_traversal_recursive_util(root, level):
    if root is None:
        return

    if level == 0:
        print(root.val, end=" ")

    bottom_level_order_traversal_recursive_util(root.left, level-1)
    bottom_level_order_traversal_recursive_util(root.right, level-1)


def bottom_level_order_traversal_recursive(root):
    if root is None:
        return

    h = height(root)
    # print("height: ", h)

    for level in range(h, -1, -1):
        bottom_level_order_traversal_recursive_util(root, level)
        print()


if __name__ == '__main__':
    for _ in range(int(input())):
        N = int(input())
        arr = list(map(int, input().split()))
        root = TreeNode(arr[0])
        for i in range(1, N):
            root = insertBST(root, arr[i])
        bottom_level_order_traversal_recursive(root)
        print()
