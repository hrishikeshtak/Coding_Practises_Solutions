#!/usr/bin/python3


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def insert(root, val):
    if root is None:
        return TreeNode(val)

    if root.val > val:
        root.left = insert(root.left, val)
    else:
        root.right = insert(root.right, val)

    return root


def inOrder(root):
    if root is None:
        return

    inOrder(root.left)
    print(root.val, end=" ")
    inOrder(root.right)


def height(root):
    if root is None:
        return 0

    return max(height(root.left), height(root.right)) + 1


def is_balanced(root):
    if root is None:
        return True

    left_height = height(root.left)
    right_height = height(root.right)

    # print(root.val, left_height, right_height)
    if abs(left_height - right_height) <= 1:
        return is_balanced(root.left) and is_balanced(root.right)

    return False


if __name__ == '__main__':
    for _ in range(int(input())):
        N = int(input())
        arr = list(map(int, input().split()))

        root = None
        for i in range(0, N):
            root = insert(root, arr[i])

        # inOrder(root)
        # print()
        if is_balanced(root):
            print("Yes")
        else:
            print("No")
