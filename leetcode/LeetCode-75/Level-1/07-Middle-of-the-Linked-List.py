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

    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None

        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if fast and fast.next is None:
                return slow
            if fast and fast.next.next is None:
                return slow.next

        return slow


if __name__ == '__main__':
    l1 = [1,2,3,4,5,6]
    l1 = [1, 2, 3]

    sll = Solution()
    head1 = sll.createSLL(l1)
    sll.displaySLL(head1)
    res = sll.middleNode(head1)
    print("Middle node:")
    sll.displaySLL(res)
