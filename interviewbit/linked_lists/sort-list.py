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


# Definition for singly-linked list.
# class ListNode:
#    def __init__(self, x):
#        self.val = x
#        self.next = None

class Solution:
    # @param A : head node of linked list
    # @return the head node in the linked list
    def sortList(self, root):
        if root is None or root.next is None:
            return root

        mid = self.findMid(root)
        t = mid.next
        mid.next = None

        return self.merge(self.sortList(root), self.sortList(t))

    def findMid(self, root, flag=True):
        if root is None:
            return root

        s = f = root
        while f.next and f.next.next:
            s = s.next
            f = f.next.next

        if f.next is None or flag:
            return s

        return s.next

    def merge(self, A, B):
        dummy = ListNode(-1)
        td = dummy

        while A and B:
            if A.val < B.val:
                dummy.next = A
                A = A.next
            else:
                dummy.next = B
                B = B.next
            dummy = dummy.next

        if A:
            dummy.next = A
        else:
            dummy.next = B

        return td.next


if __name__ == '__main__':
    root = None
    root = createSLL(root, 5)
    root = createSLL(root, 8)
    root = createSLL(root, 20)
    root = createSLL(root, 4)
    root = createSLL(root, 11)
    root = createSLL(root, 15)
    displaySLL(root)
    root = Solution().sortList(root)
    displaySLL(root)
