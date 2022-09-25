"""
92. Reverse Linked List II
"""

from typing import List, Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        first = dummy
        pos = 1
        cur = head
        while pos < left:
            first = cur
            cur = cur.next
            pos += 1
        left_node = cur
        
        # Reverse the LL
        prev_node = None
        next_node = None
        while pos <= right:
            next_node = cur.next
            cur.next = prev_node
            prev_node = cur
            cur = next_node
            pos += 1
        first.next = prev_node
        left_node.next = next_node
        return dummy.next
