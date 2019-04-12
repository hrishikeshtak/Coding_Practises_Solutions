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


def inOrderTraversal(root):
    stack = []
    cur = root
    done = False

    while not done:
        if cur:
            stack.append(cur)
            cur = cur.left
        else:
            if stack:
                cur = stack.pop()
                print(cur.val, end=" ")
                cur = cur.right
            else:
                done = True
    print()


def preOrderTraversal(root):
    stack = []
    cur = root

    stack.append(cur)

    while stack:
        cur = stack.pop()
        print(cur.val, end=" ")
        if cur.right:
            stack.append(cur.right)
        if cur.left:
            stack.append(cur.left)
    print()


def postOrderTraversal(root):
    s1 = []
    s2 = []
    cur = root

    s1.append(cur)
    while s1:
        cur = s1.pop()
        s2.append(cur.val)
        if cur.left:
            s1.append(cur.left)
        if cur.right:
            s1.append(cur.right)

    for i in s2[::-1]:
        print(i, end=" ")
    print()


if __name__ == '__main__':
    for _ in range(int(input())):
        N = int(input())
        arr = list(map(int, input().split()))
        root = TreeNode(arr[0])
        for i in range(1, N):
            root = insertBST(root, arr[i])
        preOrderTraversal(root)
        inOrderTraversal(root)
        postOrderTraversal(root)
        print()
