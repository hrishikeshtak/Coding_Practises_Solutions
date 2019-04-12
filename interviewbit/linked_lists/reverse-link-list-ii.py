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
    # @param B : integer
    # @param C : integer
    # @return the head node in the linked list
    def reverseBetween(self, root, B, C):
        if B == C:
            return root

        dummy = ListNode(-1)
        dummy.next = root
        cnt = 0
        cur = dummy
        prevNode = None
        nextNode = None
        prev = None

        # Take prev and next node
        while cur:
            if cnt == B:
                h1 = cur
                prevNode = prev
            elif cnt == C:
                nextNode = cur.next
                cur.next = None
            prev = cur
            cnt += 1
            cur = cur.next

        # reverse h1 LL
        # displaySLL(h1)
        cur = self.reverse(h1)
        # displaySLL(cur)
        # append reverse list to prev node
        prevNode.next = cur
        # append next node at end of list
        while cur.next:
            cur = cur.next
        cur.next = nextNode
        return dummy.next

    def reverse(self, root):
        cur = root
        prev = None
        temp = None

        while cur:
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp

        return prev


if __name__ == '__main__':
    root = ListNode(1)
    root.next = ListNode(2)
    root.next.next = ListNode(3)
    root.next.next.next = ListNode(4)
    root.next.next.next.next = ListNode(5)
    displaySLL(root)
    root = Solution().reverseBetween(root, 2, 4)
    displaySLL(root)
