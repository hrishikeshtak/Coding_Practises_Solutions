#!/usr/bin/python3

"""
Node is defined as
self.left (the left child of the node)
self.right (the right child of the node)
self.data (the value of the node)"""

from collections import defaultdict


class Node:
    def __init__(self, info):
        self.info = info
        self.left = None
        self.right = None
        self.level = None

    def __str__(self):
        return str(self.info)


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def create(self, val):
        if self.root is None:
            self.root = Node(val)
        else:
            current = self.root

            while True:
                if val < current.info:
                    if current.left:
                        current = current.left
                    else:
                        current.left = Node(val)
                        break
                elif val > current.info:
                    if current.right:
                        current = current.right
                    else:
                        current.right = Node(val)
                        break
                else:
                    break


def topView(root):
    # Write your code here
    if root is None:
        return None
    queue = [(root, 0)]
    hashtable = defaultdict(list)
    for node, level in queue:
        if node is not None:
            hashtable[level].append(node.info)
        if node.left is not None:
            queue.extend([(node.left, level - 1)])
        if node.right is not None:
            queue.extend([(node.right, level + 1)])
    if hashtable:
        for level in range(min(hashtable.keys()),
                           max(hashtable.keys()) + 1):
            print(hashtable[level][0], end=' ')
    else:
        return None


tree = BinarySearchTree()
t = int(input())

arr = list(map(int, input().split()))

for i in range(t):
    tree.create(arr[i])

topView(tree.root)
