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
    # @return the head node in the linked list
    def reverseList(self, root, K):
        cur = root
        prev = None
        temp = None
        cnt = 0

        while cur and cnt < K:
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp
            cnt += 1

        if temp:
            root.next = self.reverseList(temp, K)
        print(prev.val)
        return prev


if __name__ == '__main__':
    root = ListNode(1)
    root.next = ListNode(2)
    root.next.next = ListNode(3)
    root.next.next.next = ListNode(4)
    # root.next.next.next.next = ListNode(5)
    displaySLL(root)
    root = Solution().reverseList(root, 2)
    displaySLL(root)
