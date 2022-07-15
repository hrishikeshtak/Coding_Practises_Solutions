"""
24. Swap Nodes in Pairs
Given a linked list, swap every two adjacent nodes and return its head. You must solve the problem without modifying the values in the list's nodes (i.e., only nodes themselves may be changed.)

Input: head = [1,2,3,4]
Output: [2,1,4,3]
"""

from typing import List, Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cnt = 0
        if not head:
            return None

        dummy = c_dummy = ListNode(0)
        cur = head
        while cur:
            cnt += 1
            if cnt % 2 == 0:
                dummy.next = ListNode(cur.val)
                dummy = dummy.next
                if temp:
                    dummy.next = temp
                    dummy = dummy.next
                    temp = None
            else:
                temp = ListNode(cur.val)
            cur = cur.next

        if temp:
            dummy.next = temp
            dummy = dummy.next

        return c_dummy.next
        

def displaySLL(l1: Optional[ListNode]):
    cur = l1
    while cur:
        print(cur.val, end=" ")
        cur = cur.next
    print()


if __name__ == "__main__":
    # head = [1,2,3,4]
    h1 = ListNode(1)
    # h1.next = ListNode(2)
    # h1.next.next = ListNode(3)
    # h1.next.next.next = ListNode(4)

    print("h1 list:")
    displaySLL(h1)
    head = Solution().swapPairs(h1)
    print("swapPairs: ")
    displaySLL(head)
