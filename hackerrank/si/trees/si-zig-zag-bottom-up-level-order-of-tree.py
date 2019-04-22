#!/usr/bin/python3

# using Pre Order traversal

from collections import defaultdict


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


def zigzag_bottom_up_order_traversal_util(root, level, hashmap):
    if root is None:
        return

    hashmap[level].append(root.val)

    zigzag_bottom_up_order_traversal_util(root.left, level+1, hashmap)
    zigzag_bottom_up_order_traversal_util(root.right, level+1, hashmap)

    return hashmap


def zigzag_bottom_up_order_traversal(root):
    if root is None:
        return None

    hashmap = defaultdict(list)
    hashmap = zigzag_bottom_up_order_traversal_util(root, 0, hashmap)
    # print(hashmap)

    # print(sorted(hashmap, reverse=True))
    for level in sorted(hashmap, reverse=True):
        # print(key, hashmap[val])
        if level % 2 == 0:
            print(*(sorted(hashmap[level], reverse=True)), end=" ")
        else:
            print(*hashmap[level], end=" ")
    print()


if __name__ == '__main__':
    for _ in range(int(input())):
        N = int(input())
        arr = list(map(int, input().split()))
        root = TreeNode(arr[0])
        for i in range(1, N):
            root = insertBST(root, arr[i])
        zigzag_bottom_up_order_traversal(root)
