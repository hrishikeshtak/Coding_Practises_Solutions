#!/usr/bin/python3


class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


def createNode(val):
    node = ListNode(val)
    return node


def createSLL(root, val):
    node = createNode(val)
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
        print(cur.val, end=" ")
        cur = cur.next
    print()


def findMid(root, flag=True):
    if root is None:
        return root

    s = f = root
    while f.next and f.next.next:
        s = s.next
        f = f.next.next

    if f.next is None or flag:
        return s

    return s.next


if __name__ == '__main__':
    root = None
    root = createSLL(root, 5)
    root = createSLL(root, 8)
    root = createSLL(root, 20)
    root = createSLL(root, 4)
    root = createSLL(root, 11)
    root = createSLL(root, 15)
    displaySLL(root)
    cur = findMid(root, False)
    print(cur.val)
