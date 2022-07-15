"""
61. Rotate List

Given the head of a linked list, rotate the list to the right by k places.
"""

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return head
        
        length, tail = 1, head
        while tail.next:
            tail = tail.next
            length += 1
            
        k = k % length
        if k == 0:
            return head
        
        # move head to pivot and rotate
        cur = head
        for i in range(length - k - 1):
            cur = cur.next
        new_head = cur.next
        cur.next = None
        tail.next = head
        return new_head


def displaySLL(l1: Optional[ListNode]):
    cur = l1
    while cur:
        print(cur.val, end=" ")
        cur = cur.next
    print()


if __name__ == "__main__":
    # Input: head = [1,2,3,4,5], k = 2
    # Output: [4,5,1,2,3]
    h1 = ListNode(1)
    h1.next = ListNode(2)
    h1.next.next = ListNode(3)
    h1.next.next.next = ListNode(4)
    h1.next.next.next.next = ListNode(5)

    print("h1 list:")
    displaySLL(h1)
    head = Solution().rotateRight(h1, 2)
    print("rotateRight: ")
    displaySLL(head)
