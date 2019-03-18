#!/usr/bin/python3

"""
Implicit treap can be viewed as a dynamic array which supports the following
operations , each in O(logN) time :
Insert an element at any position.
Delete an element at any position.
Cut an array A[1..n] at any pos such that it is divided into two different
arrays B[1..pos] , C[pos...n] .
Merge two different arrays P[1..n1] , Q[1..n2] into a single array
R[1..n1,n+1,...n2].
"""

# import random to assign priority
from random import randint


class Node(object):
    def __init__(self, val):
        self.val = val
        self.priority = randint(1, 100)
        self.size = 1
        self.left = None
        self.right = None


class ImplicitTreap():
    def size(self, root):
        if root:
            return root.size
        return 0

    def updateSize(self, root):
        if root:
            root.size = self.size(root.left) + 1 + self.size(root.right)

    def split(self, root,
              left_subtree,
              right_subtree,
              key):
        if not root:
            left_subtree = right_subtree = None
            return left_subtree, right_subtree

        elif root.val <= key:
            self.split(
                root.right, root.right, right_subtree, key)
            left_subtree = root
        else:
            self.split(
                root.left, left_subtree, root.left, key)
            right_subtree = root

        self.updateSize(root)
        return left_subtree, right_subtree

    def merge(self, root, left, right):
        if not left or not right:
            return root
        elif left.priority > right.priority:
            self.merge(left.right, left.right, right)
            root = left
        else:
            self.merge(right.left, left, right.left)
            root = right
        self.updateSize(root)
        return root

    # def insert(self, root, node):
    #     if not root:
    #         root = node
    #     elif node.priority > root.priority:
    #         self.

    def inOrder(self, root):
        if root:
            self.inOrder(root.left)
            print("key: %s | priority: %s " % (
                root.val, root.priority), end=' ')
            if root.left:
                print("| left child: %s " % (
                    root.left.val), end=' ')
            if root.right:
                print("| right child: %s" % (
                    root.right.val))
            print()
            self.inOrder(root.right)


if __name__ == '__main__':
    treap = ImplicitTreap()
    root = None
    root = treap.insert(root, 1)
    root = treap.insert(root, 2)
    root = treap.insert(root, 3)
    root = treap.insert(root, 4)
    root = treap.insert(root, 5)
    root = treap.insert(root, 6)
    root = treap.insert(root, 7)
    root = treap.insert(root, 8)

    print("inOrder Traversal")
    treap.inOrder(root)

    print("split treaps at 4")
    left_subtree, right_subtree = treap.split(
        root, root.left, root.right, 4)

    print("inorder of Left subtree")
    treap.inOrder(left_subtree)
    print("inorder of Right subtree")
    treap.inOrder(right_subtree)
