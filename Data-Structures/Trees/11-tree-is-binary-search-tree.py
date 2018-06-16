#!/usr/bin/python3

""" Node is defined as
class node:
  def __init__(self, data):
      self.data = data
      self.left = None
      self.right = None
"""


def check_binary_search_tree_(root):
    if not root:
        return True
    stack = []
    inOrder(root, stack)
    for i in range(len(stack) - 1):
        if stack[i] >= stack[i+1]:
            return False
    return True


def inOrder(root, stack):
    if root.left:
        inOrder(root.left, stack)
    stack.append(root.data)
    if root.right:
        inOrder(root.right, stack)
