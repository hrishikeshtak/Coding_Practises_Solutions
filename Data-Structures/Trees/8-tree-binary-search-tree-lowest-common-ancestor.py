#!/usr/bin/python

"""
Node is defined as
self.left (the left child of the node)
self.right (the right child of the node)
self.data (the value of the node)
"""


def lca(root, v1, v2):
    # Enter your code here
    while(root):
        if root.data < v1 and root.data < v2:
            root = root.right
        elif root.data > v1 and root.data > v2:
            root = root.left
        else:
            return root
