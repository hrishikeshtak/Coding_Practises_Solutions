#!/usr/bin/python2


class Node(object):
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def __str__(self):
        return(str(self.data))


class BinarySearchTree(object):
    def __init__(self):
        self.root = None

    def create(self, val):
        if self.root is None:
            self.root = Node(val)
        else:
            current = self.root

            while True:
                if val < current.data:
                    if current.left:
                        current = current.left
                    else:
                        current.left = Node(val)
                        break
                elif val > current.data:
                    if current.right:
                        current = current.right
                    else:
                        current.right = Node(val)
                        break
                else:
                    break


"""
Node is defined as
self.left (the left child of the node)
self.right (the right child of the node)
self.data (the value of the node)
"""


def levelOrder(root):
    # Write code Here
    if root is None:
        return root
    queue = [root]
    while (len(queue) > 0):
        current = queue.pop(0)
        print current.data,
        if current.left:
            queue.append(current.left)
        if current.right:
            queue.append(current.right)


if __name__ == '__main__':
    tree = BinarySearchTree()
    t = int(input())

    for _ in range(t):
        val = int(input())
        tree.create(val)

    levelOrder(tree.root)
