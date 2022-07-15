"""
83. Remove Duplicates from Sorted List

Given the head of a sorted linked list, delete all duplicates such that each element appears only once. Return the linked list sorted as well.

Input: head = [1,1,2]
Output: [1,2]
"""

from typing import List, Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None

        cur = head
        dummy = c_dummy = ListNode(0)

        if cur:
            dummy.next = ListNode(cur.val)
            dummy = dummy.next
            cur = cur.next

        while cur:
            if dummy.val != cur.val:
                dummy.next = ListNode(cur.val)
                dummy = dummy.next
            cur = cur.next
        return c_dummy.next


def displaySLL(l1: Optional[ListNode]):
    cur = l1
    while cur:
        print(cur.val, end=" ")
        cur = cur.next
    print()


if __name__ == "__main__":
    # head = [1,1,2]
    h1 = ListNode(1)
    h1.next = ListNode(1)
    h1.next.next = ListNode(2)
    h1.next.next.next = ListNode(3)

    print("h1 list:")
    displaySLL(h1)
    head = Solution().deleteDuplicates(h1)
    print("deleteDuplicates: ")
    displaySLL(head)
