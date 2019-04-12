#!/usr/bin/python3

"""
Given {1,2,3,4}, reorder it to {1,4,2,3}.
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
    # @return the head node in the linked list
    def reorderList(self, root):
        if root is None:
            return root

        mid = self.findMid(root)
        head1 = root
        head2 = mid.next
        mid.next = None

        # displaySLL(head1)
        # displaySLL(head2)
        # print("Reverse head2")
        head2 = self.reverse(head2)
        # displaySLL(head2)

        # conect alternate nodes from head1 and head2
        dummy = ListNode(-1)
        cur = dummy
        while head1 or head2:
            if head1:
                cur.next = head1
                cur = cur.next
                head1 = head1.next
            if head2:
                cur.next = head2
                cur = cur.next
                head2 = head2.next

        return dummy.next

    def reverse(self, root):
        if root is None:
            return root

        cur = root
        prev = None
        temp = None

        while cur:
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp
        return prev

    def findMid(self, root, flag=True):
        if root is None:
            return root

        slow = root
        fast = root

        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        if fast.next or flag:
            return slow
        return slow.next


if __name__ == '__main__':
    root = ListNode(1)
    root.next = ListNode(2)
    root.next.next = ListNode(3)
    root.next.next.next = ListNode(4)
    # root.next.next.next.next = ListNode(5)
    displaySLL(root)
    root = Solution().reorderList(root)
    displaySLL(root)
