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
    def removeNthFromEnd(self, root, N):
        if root is None:
            return root

        cur = root

        size = self.size(root)
        # print("size: ", size)

        # If n is greater than the size of the list,
        # remove the first node of the list.
        # if first node
        pos = size - N
        # print("pos: ", pos)
        if pos <= 0:
            return root.next

        while pos > 0:
            prev = cur
            cur = cur.next
            pos -= 1
        prev.next = cur.next
        return root

    def size(self, root):
        cnt = 0
        cur = root

        while cur:
            cnt += 1
            cur = cur.next

        return cnt


if __name__ == '__main__':
    root = ListNode(1)
    root.next = ListNode(2)
    root.next.next = ListNode(3)
    root.next.next.next = ListNode(4)
    root.next.next.next.next = ListNode(5)
    displaySLL(root)
    root = Solution().removeNthFromEnd(root, 6)
    displaySLL(root)
