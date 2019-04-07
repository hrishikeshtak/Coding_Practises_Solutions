#!/usr/bin/python3


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def createNode(data):
    node = Node(data)
    return node


def createSLL(X, N):
    if X == N:
        return None

    cur = createNode(X)
    cur.next = createSLL(X+1, N)
    return cur


def displaySLL(root):
    cur = root
    while cur:
        print(cur.data, end=" ")
        cur = cur.next
    print()


def size(head):
    size = 0
    cur = head
    while cur:
        size += 1
        cur = cur.next
    return size


# Iterative
def IterativeReverseSLL(root):
    cur = root
    prev = None
    temp = None
    while cur:
        temp = cur.next
        cur.next = prev
        prev = cur
        cur = temp

    return prev


# Recursive
def RecursiveReverseSLL(root):
    if root is None or root.next is None:
        return root

    temp = RecursiveReverseSLL(root.next)
    root.next.next = root
    root.next = None
    return temp


if __name__ == '__main__':
    N = int(input())
    root = createSLL(1, N+1)
    displaySLL(root)
    print(size(root))

    # Iterative
    root = IterativeReverseSLL(root)
    displaySLL(root)
    print(size(root))

    # Recursive
    root = RecursiveReverseSLL(root)
    displaySLL(root)
    print(size(root))
