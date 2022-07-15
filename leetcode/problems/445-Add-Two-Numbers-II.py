"""
445. Add Two Numbers II

You are given two non-empty linked lists representing two non-negative integers.
The most significant digit comes first and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.
"""

from typing import Optional, List

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
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
        cur1 = self.reverseSLL(l1)
        cur2 = self.reverseSLL(l2)
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

        return self.reverseSLL(res)


def displaySLL(l1: Optional[ListNode]):
    cur = l1
    while cur:
        print(cur.val, end=" ")
        cur = cur.next
    print()


if __name__ == '__main__':
    # Input: l1 = [7,2,4,3], l2 = [5,6,4]
    # Output: [7,8,0,7]

    h1 = ListNode(7)
    h1.next = ListNode(2)
    h1.next.next = ListNode(4)
    h1.next.next.next = ListNode(3)

    h2 = ListNode(5)
    h2.next = ListNode(6)
    h2.next.next = ListNode(4)

    displaySLL(h1)
    displaySLL(h2)

    sll = Solution()
    res = sll.addTwoNumbers(h1, h2)
    print("After Sum:")
    displaySLL(res)
