#!/usr/bin/python2


class Node(object):
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def __str__(self):
        return(str(self.data))


"""
Node is defined as
self.left (the left child of the node)
self.right (the right child of the node)
self.data (the value of the node)"""


def insert(root, val):
    if root is None:
        root = Node(val)
    else:
        current = root

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
    return(root)


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
    t = int(input())

    root = None
    for _ in range(t):
        val = int(input())
        root = insert(root, val)

    levelOrder(root)
