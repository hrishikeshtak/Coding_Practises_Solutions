#!/usr/bin/python3

# Level Order Traversal
from collections import deque


class TreeNode:
    def __init__(self, K):
        self.val = K
        self.left = None
        self.right = None


def insert(root, X):
    if root is None:
        return TreeNode(X)

    if X < root.val:
        root.left = insert(root.left, X)
    else:
        root.right = insert(root.right, X)
    return root


def height(root):
    # using Level Order Traversal
    if root is None:
        print(0)
        return

    Q = deque()
    h = 0

    Q.append((root, h))
    while Q:
        # print(Q)
        cur, h = Q.popleft()
        print("%s->%s" % (cur.val, h))
        # print(h, end=" ")

        if cur.left:
            Q.append((cur.left, h+1))
        if cur.right:
            Q.append((cur.right, h+1))


# def inOrder(root):
#     if root is None:
#         return
#     inOrder(root.left)
#     print(root.val, end=" ")
#     inOrder(root.right)


if __name__ == '__main__':
    for _ in range(int(input())):
        N = int(input())
        arr = list(map(int, input().split()))

        # insert in BST
        root = None
        for i in range(0, N):
            root = insert(root, arr[i])
        height(root)
        # inOrder(root)
        print()
