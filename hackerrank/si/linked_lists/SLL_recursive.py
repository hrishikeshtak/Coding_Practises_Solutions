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


if __name__ == '__main__':
    N = int(input())
    root = createSLL(1, N+1)
    displaySLL(root)
    print(size(root))
