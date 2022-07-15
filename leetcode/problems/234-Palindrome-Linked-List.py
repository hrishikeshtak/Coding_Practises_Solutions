"""
234. Palindrome Linked List

Given the head of a singly linked list, return true if it is a palindrome.
"""

from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False

        length = self.size(head)
        # print(f"length: {length}")
        if length == 1:
            return True

        mid = self.findMid(head, length)
        # print(f"mid: {mid.val}")
        # break LL into two LL, one till mid and next from mid+1
        cur1 = head
        cur2 = mid.next
        mid.next = None
        # displaySLL(cur1)
        # displaySLL(cur2)

        # if length is odd, then skip first node from cur2
        if length % 2 != 0:
            cur2 = cur2.next

        # reverse second LL
        cur2 = self.reverseList(cur2)
        # print("reverseList")
        # displaySLL(cur2)

        while cur1 and cur2:
            if cur1.val != cur2.val:
                return False
            cur1 = cur1.next
            cur2 = cur2.next
        return True

    def reverseList(self, head):
        if not head:
            return head

        temp = prev = None
        cur = head

        while cur:
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp
        return prev

    def findMid(self, head, length):
        # find mid of LL
        # if length is odd then mid is (length / 2) + 1 else mid is (length / 2)
        if length % 2 != 0:
            mid = (length // 2) + 1
        else:
            mid = (length // 2)

        # print(f"mid: {mid}")
        prev = cur = head

        # get mid pointer
        cnt = 1
        while cnt < mid:
            prev = cur
            cur = cur.next
            cnt += 1

        if length % 2 != 0:
            return prev
        return cur

    def size(self, head: ListNode):
        cnt = 0
        cur = head
        while cur:
            cnt += 1
            cur = cur.next

        return cnt


def displaySLL(l1: Optional[ListNode]):
    cur = l1
    while cur:
        print(cur.val, end=" ")
        cur = cur.next
    print()


if __name__ == "__main__":
    h1 = ListNode(1)
    h1.next = ListNode(2)
    # h1.next.next = ListNode(2)
    # h1.next.next.next = ListNode(1)
    # h1.next.next.next.next = ListNode(1)

    print("h1 list:")
    displaySLL(h1)
    status = Solution().isPalindrome(h1)
    print(f"isPalindrome: {status}")
