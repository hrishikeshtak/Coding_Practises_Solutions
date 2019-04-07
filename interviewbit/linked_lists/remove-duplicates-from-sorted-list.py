#!/usr/bin/python3


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
        cur = root
        while cur.next:
            if cur.val == cur.next.val:
                cur.next = cur.next.next
            else:
                cur = cur.next
        return root


if __name__ == '__main__':
    root = None
    root = createSLL(root, 1)
    root = createSLL(root, 2)
    root = createSLL(root, 2)
    root = createSLL(root, 3)
    root = createSLL(root, 3)
    root = createSLL(root, 3)
    root = createSLL(root, 4)
    root = createSLL(root, 5)
    root = createSLL(root, 5)
    displaySLL(root)
    root = Solution().deleteDuplicates(root)
    displaySLL(root)
