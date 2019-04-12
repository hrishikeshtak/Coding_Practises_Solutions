#!/usr/bin/python3

"""
Given a linked list and a value x, partition it such that all nodes
less than x come before nodes greater than or equal to x.

You should preserve the original relative order of the nodes in each
of the two partitions.

For example,
Given 1->4->3->2->5->2 and x = 3,
return 1->2->2->4->3->5.
"""


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
    # @return the head node in the linked list
    def partition(self, root, N):
        if root is None:
            return root

        dummy = ListNode(-1)
        temp = dummy
        dummy1 = ListNode(-1)
        temp1 = dummy1
        cur = root
        lastNode = None

        while cur:
            if cur.val >= N:
                dummy1.next = cur
                dummy1 = dummy1.next
            else:
                dummy.next = cur
                dummy = dummy.next
                lastNode = cur
            cur = cur.next

        dummy1.next = None
        # displaySLL(temp.next)
        # displaySLL(temp1.next)
        if temp.next is None:
            return temp1.next
        elif temp1.next is None:
            return temp.next

        lastNode.next = temp1.next
        return temp.next


if __name__ == '__main__':
    root = ListNode(1)
    # root.next = ListNode(4)
    # root.next.next = ListNode(3)
    # root.next.next.next = ListNode(2)
    # root.next.next.next.next = ListNode(5)
    # root.next.next.next.next.next = ListNode(2)
    displaySLL(root)
    root = Solution().partition(root, 1)
    displaySLL(root)
