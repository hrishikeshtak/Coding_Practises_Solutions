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


class Solution:
    # @param A : head node of linked list
    # @return the head node in the linked list
    def insertionSortList(self, root):
        if root is None:
            return root

        cur = root
        # take first node in sort list
        sorted_head = ListNode(cur.val)

        cur = cur.next
        # insert data in sorted list
        while cur:
            node = ListNode(cur.val)
            if cur.val < sorted_head.val:
                node.next = sorted_head
                sorted_head = node
            else:
                current = sorted_head
                while current.next and current.next.val < cur.val:
                    current = current.next

                node.next = current.next
                current.next = node
            cur = cur.next

        return sorted_head


if __name__ == '__main__':
    root = ListNode(1)
    root.next = ListNode(2)
    root.next.next = ListNode(4)
    root.next.next.next = ListNode(3)
    # root.next.next.next.next = ListNode(5)
    displaySLL(root)
    root = Solution().insertionSortList(root)
    displaySLL(root)
