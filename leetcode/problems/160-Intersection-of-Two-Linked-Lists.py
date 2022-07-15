"""
160. Intersection of Two Linked Lists
Given the heads of two singly linked-lists headA and headB,
return the node at which the two lists intersect.
If the two linked lists have no intersection at all, return null.
"""

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        # Approach: Using HashMap to store nodes

        cur = headA
        cache = set()
        while cur:
            cache.add(cur)
            cur = cur.next

        cur = headB
        while cur:
            if cur in cache:
                return cur
            cur = cur.next
        return None
