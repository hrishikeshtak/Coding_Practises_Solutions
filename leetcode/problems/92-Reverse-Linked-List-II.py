"""
92. Reverse Linked List II

Given the head of a singly linked list and two integers left and right where left <= right,
reverse the nodes of the list from position left to position right, and return the reversed list.
"""

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        
        dummy = ListNode(0, head)
        first = dummy
        pos = 1
        cur = head
        
        while pos < left:
            first = cur
            cur = cur.next
            pos += 1
        # store position of left node
        left_node = cur

        # reverse the nodes from left to right
        prev_node = next_node = None
        while pos <= right:
            next_node = cur.next
            cur.next = prev_node
            prev_node = cur
            cur = next_node
            pos += 1

        # update the pointer
        first.next = prev_node
        left_node.next = next_node
        return dummy.next


def displaySLL(l1: Optional[ListNode]):
    cur = l1
    while cur:
        print(cur.val, end=" ")
        cur = cur.next
    print()


if __name__ == "__main__":
    # Input: head = [1,2,3,4,5], left = 2, right = 4
    # Output: [1,4,3,2,5]
    h1 = ListNode(1)
    h1.next = ListNode(2)
    h1.next.next = ListNode(3)
    h1.next.next.next = ListNode(4)
    h1.next.next.next.next = ListNode(5)

    print("h1 list:")
    displaySLL(h1)
    head = Solution().reverseBetween(h1, 2, 4)
    print("reverseBetween: ")
    displaySLL(head)
