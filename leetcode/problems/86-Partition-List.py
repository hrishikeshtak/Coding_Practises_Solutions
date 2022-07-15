"""
86. Partition List

Given the head of a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.

You should preserve the original relative order of the nodes in each of the two partitions.

Input: head = [1,4,3,2,5,2], x = 3
Output: [1,2,2,4,3,5]
"""

from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        if not head:
            return head

        lt_dummy = ListNode(0)
        ge_dummy = ListNode(0)
        dummy = lt_dummy
        c_dummy = ge_dummy

        cur = head
        while cur:
            if cur.val < x:
                temp = ListNode(cur.val)
                lt_dummy.next = temp
                lt_dummy = lt_dummy.next
            else:
                temp = ListNode(cur.val)
                ge_dummy.next = temp
                ge_dummy = ge_dummy.next
            cur = cur.next

        if dummy.next and c_dummy.next:
            lt_dummy.next = c_dummy.next
        elif not dummy.next and c_dummy.next:
            dummy.next = c_dummy.next

        return dummy.next


def displaySLL(l1: Optional[ListNode]):
    cur = l1
    while cur:
        print(cur.val, end=" ")
        cur = cur.next
    print()


if __name__ == "__main__":
    # head = [1,4,3,2,5,2], x = 3
    h1 = ListNode(1)
    h1.next = ListNode(4)
    h1.next.next = ListNode(3)
    h1.next.next.next = ListNode(2)
    h1.next.next.next.next = ListNode(5)
    h1.next.next.next.next.next = ListNode(2)

    print("h1 list:")
    displaySLL(h1)
    head = Solution().partition(h1, 4)
    print("partition: ")
    displaySLL(head)
