#!/usr/bin/python3

# diameter of the tree. Diameter is defined as the number of nodes on
# the longest path between 2 nodes of the tree.

# O(N2)


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def insert(root, key):
    if root is None:
        return TreeNode(key)

    if root.val < key:
        root.right = insert(root.right, key)
    else:
        root.left = insert(root.left, key)

    return root


def inorder(root):
    if root is None:
        return

    inorder(root.left)
    print(root.val, end=" ")
    inorder(root.right)


def height(root):
    if root is None:
        return 0

    return max(height(root.left), height(root.right)) + 1


def diameter(root):
    if root is None:
        return 0

    lheight = height(root.left)
    rheight = height(root.right)

    ldiameter = diameter(root.left)
    rdiameter = diameter(root.right)

    return max(lheight + rheight + 1, max(ldiameter, rdiameter))


if __name__ == '__main__':
    for _ in range(int(input())):
        N = int(input())
        arr = list(map(int, input().split()))
        root = None
        for i in range(0, N):
            root = insert(root, arr[i])
        # inorder(root)
        # print()
        print(diameter(root))
