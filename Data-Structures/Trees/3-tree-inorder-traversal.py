#!/usr/bin/python

"""
Node is defined as
self.left (the left child of the node)
self.right (the right child of the node)
self.data (the value of the node)
"""


def inOrder(root):
    # Write your code here
    if not root:
        return
    # print(root.data, end='')  # python3
    inOrder(root.left)
    print(root.data),  # python2
    inOrder(root.right)
