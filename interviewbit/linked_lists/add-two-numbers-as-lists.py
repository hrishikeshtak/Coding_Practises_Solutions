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
    # @param B : head node of linked list
    # @return the head node in the linked list
    def addTwoNumbers(self, root1, root2):
        if root1 is None and root2 is None:
            return root1
        elif root1 is None:
            return root2
        elif root2 is None:
            return root1

        # print("after reverse: ")
        # root1 = self.reverse(root1)
        # root2 = self.reverse(root2)
        # displaySLL(root1)
        # displaySLL(root2)

        dummy = ListNode(-1)
        cur = dummy
        carry = 0

        while root1 and root2:
            num = root1.val + root2.val + carry
            carry = num // 10
            num = num % 10
            cur.next = ListNode(num)
            cur = cur.next
            root1 = root1.next
            root2 = root2.next

        while root1:
            num = root1.val + carry
            carry = num // 10
            num = num % 10
            cur.next = ListNode(num)
            cur = cur.next
            root1 = root1.next

        while root2:
            num = root2.val + carry
            carry = num // 10
            num = num % 10
            cur.next = ListNode(num)
            cur = cur.next
            root2 = root2.next

        if carry:
            cur.next = ListNode(carry)
            cur = cur.next

        return (dummy.next)

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


if __name__ == '__main__':
    root = ListNode(2)
    root.next = ListNode(4)
    root.next.next = ListNode(3)
    root1 = ListNode(5)
    root1.next = ListNode(6)
    root1.next.next = ListNode(4)

    root = ListNode(9)
    root.next = ListNode(9)
    root.next.next = ListNode(1)
    root1 = ListNode(1)

    displaySLL(root)
    displaySLL(root1)
    root = Solution().addTwoNumbers(root, root1)
    displaySLL(root)
