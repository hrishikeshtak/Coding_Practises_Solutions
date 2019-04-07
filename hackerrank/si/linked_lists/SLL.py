#!/usr/bin/python3


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def createNode(data):
    node = Node(data)
    return node


def createSLL(head, N):
    if head is None:
        head = createNode(1)

    cur = head
    for i in range(2, N+1):
        cur.next = createNode(i)
        cur = cur.next
    return head


def displaySLL(root):
    cur = root
    while cur:
        print(cur.data, end=" ")
        cur = cur.next
    print()


if __name__ == '__main__':
    N = int(input())
    root = None
    root = createSLL(root, N)
    displaySLL(root)
