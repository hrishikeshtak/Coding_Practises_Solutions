"""
Linked List Cycle II
"""

"""
Middle of the Linked List
"""
from typing import List, Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def createSLL(self, lst: List[int]):
        if not lst:
            return None

        head = None
        cur = None

        for i in lst:
            temp = ListNode(val=i)
            if head is None:
                head = temp
                cur = head
            else:
                cur.next = temp
                cur = cur.next
        return head

    def displaySLL(self, l1: Optional[ListNode]):
        cur = l1
        while cur:
            print(cur.val, end=" ")
            cur = cur.next
        print()

    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                break
        else:
            return None

        pointer = head
        while pointer != fast:
            pointer = pointer.next
            fast = fast.next

        return pointer



if __name__ == '__main__':
    head = ListNode(50)
    head.next = ListNode(20)
    head.next.next = ListNode(15)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(10)

    # Create a loop for testing
    head.next.next.next.next.next = head.next.next

    res = Solution().detectCycle(head)
    if not res:
        print("No Cycle detected")
    else:
        print(f"Cycle Detected at Node: {res.val}")
