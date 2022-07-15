"""
82. Remove Duplicates from Sorted List II

Given the head of a sorted linked list, delete all nodes that have duplicate numbers,
leaving only distinct numbers from the original list. Return the linked list sorted as well.
"""

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Time: O(n)
        # Space: O(1)
        if not head:
            return None

        cur = head
        dummy = c_dummy = ListNode(0)

        key = cur.val
        cnt = 0
        while cur:
            print(f"key: {key} cnt: {cnt}")
            if cur.val == key:
                cnt += 1
            elif cur.val != key:
                if cnt == 1:
                    dummy.next = ListNode(key)
                    dummy = dummy.next

                # update key value and initialize cnt to 1
                key = cur.val
                cnt = 1
            cur = cur.next

        if cnt == 1:
            dummy.next = ListNode(key)
            dummy = dummy.next

        return c_dummy.next



def displaySLL(l1: Optional[ListNode]):
    cur = l1
    while cur:
        print(cur.val, end=" ")
        cur = cur.next
    print()


if __name__ == "__main__":
    # Input: head = [1,1,1,2,3]
    # Output: [2,3]
    h1 = ListNode(1)
    h1.next = ListNode(2)
    h1.next.next = ListNode(3)
    h1.next.next.next = ListNode(3)
    h1.next.next.next.next = ListNode(3)
    h1.next.next.next.next.next = ListNode(4)
    h1.next.next.next.next.next.next = ListNode(4)
    h1.next.next.next.next.next.next.next = ListNode(5)

    print("h1 list:")
    displaySLL(h1)
    head = Solution().deleteDuplicates(h1)
    print("Distinct numbers: ")
    displaySLL(head)
