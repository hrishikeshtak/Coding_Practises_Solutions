#!/usr/bin/python3

# Unique elements from sorted list


class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


def createNode(val):
    node = Node(val)
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
    def deleteDuplicates(self, root):
        dummy = createNode(-1)
        prev = dummy
        cur = root
        dummy.next = cur

        while cur:
            while cur.next and prev.next.val == cur.next.val:
                cur = cur.next

            if prev.next == cur:
                prev = prev.next
            else:
                prev.next = cur.next

            cur = cur.next

        return dummy.next


if __name__ == '__main__':
    root = None
    root = createSLL(root, 1)
    root = createSLL(root, 2)
    root = createSLL(root, 3)
    root = createSLL(root, 3)
    root = createSLL(root, 4)
    root = createSLL(root, 4)
    root = createSLL(root, 5)
    displaySLL(root)
    root = Solution().deleteDuplicates(root)
    displaySLL(root)
