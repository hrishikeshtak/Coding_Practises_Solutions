#!/usr/bin/python3
import random


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

    X = random.randint(1, N)
    cur = createNode(X)
    cur.next = createSLL(X, N)
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


# Delete by position
def delete(head, pos):
    cur = head
    if cur is None or pos < 0 or pos >= size(head):
        return cur

    if pos == 0:
        return head.next

    cnt = 1
    while cnt != pos:
        cur = cur.next
        cnt += 1
    cur.next = cur.next.next
    return head


# DeleteAll instance of given number
def deleteAll(head, X):
    cur = head
    if cur is None:
        return cur

    while cur.next:
        if cur.next.data == X:
            cur.next = cur.next.next
        else:
            cur = cur.next

    if head.data == X:
        return head.next

    return head


if __name__ == '__main__':
    N = int(input())
    root = createSLL(1, N+1)
    displaySLL(root)
    print(size(root))

    # # Delete by position
    # root = delete(root, 5)
    # displaySLL(root)
    # print(size(root))

    # DeleteAll instance of given number
    # import pdb; pdb.set_trace()
    root = deleteAll(root, 2)
    displaySLL(root)
    print(size(root))
