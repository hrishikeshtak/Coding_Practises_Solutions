"""
Merge Two Sorted Lists
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

    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # take dummy node pointing to dummy val
        dummy = ListNode(-1)

        head = None
        cur1 = list1
        cur2 = list2

        while cur1 and cur2:
            if cur1.val <= cur2.val:
                temp = ListNode(cur1.val)
                cur1 = cur1.next
            else:
                temp = ListNode(cur2.val)
                cur2 = cur2.next

            # first node
            if head is None:
                head = temp
                dummy.next = head
            else:
                head.next = temp
                head = temp

        # if one of the LL is over
        if cur1:
            # if one of the LL is empty
            if not head:
                dummy.next = cur1
            else:
                head.next = cur1
        elif cur2:
            # if one of the LL is empty
            if not head:
                dummy.next = cur2
            else:
                head.next = cur2

        return dummy.next


if __name__ == '__main__':
    list1 = []
    list2 = [0]


    sll = Solution()
    head1 = sll.createSLL(list1)
    sll.displaySLL(head1)
    head2 = sll.createSLL(list2)
    sll.displaySLL(head2)
    res = sll.mergeTwoLists(head1, head2)
    print("After Merge:")
    sll.displaySLL(res)
