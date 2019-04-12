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
    def detectCycle(self, root):
        if root is None:
            return root

        slow = root
        fast = root
        loop = False

        while slow and fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                loop = True
                break

        if not loop:
            return None
        else:
            slow = root
            while slow != fast:
                slow = slow.next
                fast = fast.next
            return slow


if __name__ == '__main__':
    root = ListNode(1)
    root.next = ListNode(2)
    root.next.next = ListNode(3)
    root.next.next.next = ListNode(4)
    # cycle
    root.next.next.next.next = root.next.next
    # displaySLL(root)
    cur = Solution().detectCycle(root)
    if cur:
        print(cur.val)
    else:
        print("No")
