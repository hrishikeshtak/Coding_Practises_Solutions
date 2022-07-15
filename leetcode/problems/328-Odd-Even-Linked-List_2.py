"""
328. Odd Even Linked List
Given the head of a singly linked list, group all the nodes with odd indices together followed by the nodes with even indices,
and return the reordered list.

The first node is considered odd, and the second node is even, and so on.

Note that the relative order inside both the even and odd groups should remain as it was in the input.

You must solve the problem in O(1) extra space complexity and O(n) time complexity.
"""

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # if LL have <= 2 nodes, do not do any operations
        if head is None or head.next is None or head.next.next is None:
            return head

        # find jumps to reach to end pointer
        end = head
        cur = head
        jumps = 0

        while end.next:
            end = end.next
            jumps += 1
        # print(f"jumps to reach end pointer: {end.val} is {jumps}")

        # calculate how many steps required to arrange LL in odd even fashion
        if jumps % 2 == 0:
            steps = jumps // 2
        else:
            steps = (jumps // 2) + 1
        cnt = 0
        while cnt < steps:
            temp = cur.next
            cur.next = cur.next.next
            end.next = temp
            temp.next = None
            cur = cur.next
            end = end.next
            cnt += 1

        return head


def displaySLL(l1: Optional[ListNode]):
    cur = l1
    while cur:
        print(cur.val, end=" ")
        cur = cur.next
    print()


if __name__ == "__main__":
    # Input: head = [1,2,3,4,5]
    # Output: [1,3,5,2,4]
    h1 = ListNode(1)
    h1.next = ListNode(2)
    h1.next.next = ListNode(3)
    h1.next.next.next = ListNode(4)
    h1.next.next.next.next = ListNode(5)

    print("h1 list:")
    displaySLL(h1)
    head = Solution().oddEvenList(h1)
    print("oddEvenList: ")
    displaySLL(head)
