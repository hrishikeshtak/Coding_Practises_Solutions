#!/usr/bin/python3


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def createNode(data):
    node = Node(data)
    return node


def createSLL(root, data):
    node = createNode(data)
    if root is None:
        return node

    cur = root
    while cur.next:
        cur = cur.next
    cur.next = node
    return root


def displaySLL(root):
    cur = root
    while cur:
        print(cur.data, end=" ")
        cur = cur.next
    print()


def distinct(root):
    cur = root
    while cur.next:
        if cur.data == cur.next.data:
            cur.next = cur.next.next
        else:
            cur = cur.next
    return root


if __name__ == '__main__':
    root = None
    root = createSLL(root, 1)
    root = createSLL(root, 2)
    root = createSLL(root, 2)
    root = createSLL(root, 3)
    root = createSLL(root, 3)
    root = createSLL(root, 3)
    root = createSLL(root, 4)
    root = createSLL(root, 5)
    root = createSLL(root, 5)
    displaySLL(root)
    root = distinct(root)
    displaySLL(root)
