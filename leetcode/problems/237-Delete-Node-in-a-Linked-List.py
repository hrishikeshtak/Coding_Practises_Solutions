"""
237. Delete Node in a Linked List

Write a function to delete a node in a singly-linked list. You will not be given access to the head of the list,
instead you will be given access to the node to be deleted directly.

It is guaranteed that the node to be deleted is not a tail node in the list.
"""

from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """

        prev = node
        cur = node
        cur = cur.next
        while cur:
            # update the val of node
            prev.val = cur.val
            # if it is a tail node, do not update prev node
            if cur.next is None:
                break
            prev = cur
            cur = cur.next
        # remove tail node
        prev.next = None

def displaySLL(l1: Optional[ListNode]):
    cur = l1
    while cur:
        print(cur.val, end=" ")
        cur = cur.next
    print()


if __name__ == "__main__":
    h1 = ListNode(4)
    h1.next = ListNode(5)
    h1.next.next = ListNode(1)
    h1.next.next.next = ListNode(9)
    # h1.next.next.next.next = ListNode(1)

    print("h1 list:")
    displaySLL(h1)
    Solution().deleteNode(h1.next.next)
    print(f"deleteNode:")
    displaySLL(h1)
