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


def removeNthFromLast(head, K):
    """
    use two pointers ref, cur
    first move ref pointer K places, then start moving cur pointer.
    If ref pointer moves to end then print cur pointer
    """
    if head is None:
        return head

    dummy = Node(-1)
    dummy.next = head
    td = dummy

    ref = cur = head
    cnt = 0
    while cnt < K:
        ref = ref.next
        cnt += 1

    while ref:
        cur = cur.next
        ref = ref.next
        dummy = dummy.next

    dummy.next = cur.next

    return td.next


if __name__ == '__main__':
    head = None
    head = createSLL(head, 5)
    head = createSLL(head, 4)
    head = createSLL(head, 3)
    head = createSLL(head, 2)
    head = createSLL(head, 1)

    displaySLL(head)
    head = removeNthFromLast(head, 2)
    displaySLL(head)
