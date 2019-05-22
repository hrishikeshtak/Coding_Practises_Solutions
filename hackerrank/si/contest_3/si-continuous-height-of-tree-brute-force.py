#!/usr/bin/python3


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
    if root is None:
        return -1

    return max(height(root.left), height(root.right)) + 1


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
            # print("height: ", height(root))
            print(height(root), end=" ")
        # inOrder(root)
        print()
