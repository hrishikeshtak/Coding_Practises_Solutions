#!/usr/bin/python3


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def createSLL(head, data):
    node = Node(data)
    node.next = head
    head = node
    return head


def displaySLL(head):
    cur = head
    while cur:
        print(cur.data, end=" ")
        cur = cur.next
    print()


def printNthFromLast(head, K):
    """
    use two pointers ref, cur
    first move ref pointer K places, then start moving cur pointer.
    If ref pointer moves to end then print cur pointer
    """
    ref = cur = head
    cnt = 0
    while cnt < K:
        ref = ref.next
        cnt += 1

    while ref:
        cur = cur.next
        ref = ref.next
    return cur.data


if __name__ == '__main__':
    head = None
    head = createSLL(head, 20)
    head = createSLL(head, 4)
    head = createSLL(head, 15)
    head = createSLL(head, 35)

    displaySLL(head)
    print(printNthFromLast(head, 3))
