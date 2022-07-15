"""
Add Two Numbers

You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.
"""

from typing import Optional, List

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

    def reverseSLL(self, l1: Optional[ListNode]):
        head = l1
        cur = head
        prev = None

        while cur:
            head = cur.next
            cur.next = prev
            prev = cur
            cur = head

        return prev


    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        cur1 = l1
        cur2 = l2
        carry = 0
        # result SLL
        res = None
        temp = None
        prev = None

        while cur1 or cur2:
            _sum = carry + (cur1.val if cur1 else 0) + (cur2.val if cur2 else 0)

            # update carry for next calculation
            carry = 1 if _sum >= 10 else 0
            # update sum if sum >= 10
            _sum = _sum % 10

            temp = ListNode(_sum)
            if res is None:
                res = temp
            else:
                prev.next = temp

            prev = temp

            if cur1:
                cur1 = cur1.next
            if cur2:
                cur2 = cur2.next

        if carry > 0:
            temp.next = ListNode(carry)

        return res


if __name__ == '__main__':
    l1 = [2,4,3]
    l2 = [5,6,4]

    l1 = [0]
    l2 = [0]

    l1 = [9,9,9,9,9,9,9]
    l2 = [9,9,9,9]

    sll = Solution()
    head1 = sll.createSLL(l1)
    head2 = sll.createSLL(l2)

    sll.displaySLL(head1)
    sll.displaySLL(head2)
    res = sll.addTwoNumbers(head1, head2)
    print("After Sum:")
    sll.displaySLL(res)
