"""
203. Remove Linked List Elements

Given the head of a linked list and an integer val, remove all the nodes of the linked list that
has Node.val == val, and return the new head.

Input: head = [1,2,6,3,4,5,6], val = 6
Output: [1,2,3,4,5]
"""

from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        if not head:
            return head

        prev = dummy = ListNode(0, head)
        cur = head

        while cur:
            if cur.val == val:
                prev.next = cur.next
            else:
                prev = cur
            cur = cur.next

        return dummy.next


def displaySLL(l1: Optional[ListNode]):
    cur = l1
    while cur:
        print(cur.val, end=" ")
        cur = cur.next
    print()


if __name__ == "__main__":
	# Input: head = [1,2,6,3,4,5,6], val = 6
	# Output: [1,2,3,4,5]
    # h1 = ListNode(1)
    # h1.next = ListNode(2)
    # h1.next.next = ListNode(6)
    # h1.next.next.next = ListNode(3)
    # h1.next.next.next.next = ListNode(4)
    # h1.next.next.next.next.next = ListNode(5)
    # h1.next.next.next.next.next.next = ListNode(6)


    h1 = ListNode(1)
    h1.next = ListNode(1)
    h1.next.next = ListNode(1)
    h1.next.next.next = ListNode(1)
    print("h1 list:")
    displaySLL(h1)
    # head = Solution().removeElements(None, 1)
    head = Solution().removeElements(h1, 1)
    print("removeElements: ")
    displaySLL(head)
