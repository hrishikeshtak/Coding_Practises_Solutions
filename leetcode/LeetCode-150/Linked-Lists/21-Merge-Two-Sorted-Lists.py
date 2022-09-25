"""
21. Merge Two Sorted Lists

You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the
first two lists.

Return the head of the merged linked list.
"""

from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        if not list1 and not list2:
            return None
        
        dummy = ListNode(-1)
        cur_dummy = dummy
        
        while list1 and list2:
            if list1.val <= list2.val:
                temp = ListNode(list1.val)
                cur_dummy.next = temp
                list1 = list1.next
            else:
                temp = ListNode(list2.val)
                cur_dummy.next = temp
                list2 = list2.next
            cur_dummy = cur_dummy.next
        
        if list1:
            cur_dummy.next = list1
        elif list2:
            cur_dummy.next = list2
        
        return dummy.next
            
            
