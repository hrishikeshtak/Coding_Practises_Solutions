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
#   def __init__(self, x):
#       self.val = x
#       self.next = None

class Solution:
    # @param A : head node of linked list
    # @return an integer
    def lPalin(self, root):
        mid = self.findMid(root)
        size = self.size(root)
        # print("size: ", size)
        h1 = mid.next
        mid.next = None
        # displaySLL(root)
        # displaySLL(h1)
        # print("After reverse: ")
        root = self.reverse(root)
        # displaySLL(root)
        # displaySLL(h1)

        # if length of LL is odd then skip first node
        if size & 1:
            root = root.next

        while root and h1:
            if root.val != h1.val:
                return 0
            root = root.next
            h1 = h1.next

        return 1

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

    def findMid(self, root, flag=True):
        if root is None:
            return root

        slow = root
        fast = root

        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        if fast.next is None or flag is True:
            return slow

        return slow.next

    def size(self, root):
        cur = root
        cnt = 0
        while cur:
            cnt += 1
            cur = cur.next
        return cnt


if __name__ == '__main__':
    root = ListNode(1)
    root.next = ListNode(2)
    root.next.next = ListNode(1)
    # root.next.next= ListNode(2)
    # root.next.next.next.next = ListNode(1)
    displaySLL(root)
    cur = Solution().lPalin(root)
    if cur == 1:
        print("Palindrome")
    else:
        print("Not Palindrome")
