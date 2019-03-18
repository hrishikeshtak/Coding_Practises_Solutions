#!/usr/bin/python3

""" Treap | (Implementation of Search and Insert)
A Treap is a cartesian tree.
A Cartesian Tree is basically a tree in which each node stores a pair
(Bk,Hk) where
Bk => Corresponds to value of a node wrt BST
Hk => Corresponds to Priority of a node wrt Heap.
"""

# import random to assign priority
from random import randint


class Node(object):
    def __init__(self, val):
        self.key = val
        self.priority = randint(1, 100)
        self.left = None
        self.right = None


"""
* T1, T2 and T3 are subtrees of the tree rooted with y
  (on left side) or x (on right side)
                y                               x
               / \     Right Rotation          /  \
              x   T3   – – – – – – – >        T1   y
             / \       < - - - - - - -            / \
            T1  T2     Left Rotation            T2  T3 */

// A utility function to right rotate subtree rooted with y
// See the diagram given above.
"""


class Treap():
    def rightRotate(self, y):
        x = y.left
        t2 = x.right

        # perform rotation
        x.right = y
        y.left = t2
        # return new root
        return x

    def leftRotate(self, x):
        y = x.right
        t2 = y.left

        # perform rotation
        y.left = x
        x.right = t2

        # return new root
        return y

    def insert(self, root, key):
        if not root:
            return (Node(key))

        # if key is smaller than root.ket
        if key <= root.key:
            # insert in left sub tree
            root.left = self.insert(root.left, key)

            # Fix MAX heap property if it is violated
            if root.left.priority > root.priority:
                root = self.rightRotate(root)
        else:
            # insert in right sub tree
            root.right = self.insert(root.right, key)

            # Fix MAX heap property
            if root.right.priority > root.priority:
                root = self.leftRotate(root)

        return root

    def inOrder(self, root):
        if root:
            self.inOrder(root.left)
            print("key: %s | priority: %s " % (
                root.key, root.priority), end=' ')
            if root.left:
                print("| left child: %s " % (
                    root.left.key), end=' ')
            if root.right:
                print("| right child: %s" % (
                    root.right.key))
            print()
            self.inOrder(root.right)


if __name__ == '__main__':
    treap = Treap()
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
