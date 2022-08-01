"""
19. Remove Nth Node From End of List

Given the head of a linked list, remove the nth node from the end of the list and return its head.
Follow up: Could you do this in one pass?
"""

from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

        
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head:
            return head
        
        # take dummy node
        dummy = ListNode(-1, head)
        td = dummy
        
        cur = ref = head
        # point to nth node from left
        while n > 0:
            ref = ref.next
            n -= 1
        
        while ref:
            cur = cur.next
            ref = ref.next
            td = td.next
        
        td.next = cur.next
        return dummy.next
