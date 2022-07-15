"""
Reverse Linked List
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

    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = head
        prev = None

        while cur:
            head = cur.next
            cur.next = prev
            prev = cur
            cur = head

        return prev


if __name__ == '__main__':
    l1 = [2,4,3]

    l1 = [0]

    l1 = []


    sll = Solution()
    head1 = sll.createSLL(l1)
    sll.displaySLL(head1)
    res = sll.reverseList(head1)
    print("After Reverse:")
    sll.displaySLL(res)
