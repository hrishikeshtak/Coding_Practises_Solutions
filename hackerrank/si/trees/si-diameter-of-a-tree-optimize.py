#!/usr/bin/python3

# diameter of the tree. Diameter is defined as the number of nodes on
# the longest path between 2 nodes of the tree.

# O(N)
ans = 0


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


def diameter(root):
    global ans
    if root is None:
        return 0

    ans = 0
    h = diameter_util(root)
    # print(h, ans)
    return ans


def diameter_util(root):
    global ans
    if root is None:
        return 0

    lheight = diameter_util(root.left)
    rheight = diameter_util(root.right)

    ans = max(ans, lheight + rheight + 1)

    return 1 + max(lheight, rheight)


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
