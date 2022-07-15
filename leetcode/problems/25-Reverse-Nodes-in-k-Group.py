"""
25. Reverse Nodes in k-Group

Given the head of a linked list, reverse the nodes of the list k at a time, and return the modified list.

k is a positive integer and is less than or equal to the length of the linked list.
If the number of nodes is not a multiple of k then left-out nodes, in the end, should remain as it is.

You may not alter the values in the list's nodes, only nodes themselves may be changed.
Example 1:

Input: head = [1,2,3,4,5], k = 2
Output: [2,1,4,3,5]
"""

from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    # def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
    #     if not head:
    #         return None

    #     temp = prev = None
    #     cur = head
    #     cnt = 0

    #     while cur and cnt < k:
    #         # temp stores address of next node
    #         temp = cur.next
    #         cur.next = prev
    #         prev = cur
    #         cur = temp
    #         cnt += 1

    #     print(f"cnt: {cnt}")
    #     if temp:
    #         head.next = self.reverseKGroup(temp, k)

    #     return prev

    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return head

        dummy = ListNode(0, head)
        # first node of group
        group_prev = dummy

        while True:
            kth_node = self.getKth(group_prev, k)

            # If the number of nodes is not a multiple of k then left-out nodes
            if kth_node is None:
                break

            # next group first element
            group_next = kth_node.next

            prev, cur = group_next, group_prev.next
            while cur != group_next:
                temp = cur.next
                cur.next = prev
                prev = cur
                cur = temp

            # to adjust the next group start node
            temp = group_prev.next
            group_prev.next = kth_node
            group_prev = temp

        return dummy.next

    def getKth(self, cur, k):
        while cur and k > 0:
            cur = cur.next
            k -= 1
        return cur


def displaySLL(l1: Optional[ListNode]):
    cur = l1
    while cur:
        print(cur.val, end=" ")
        cur = cur.next
    print()


if __name__ == "__main__":
    # head = [1,2,3,4,5], k = 3
    h1 = ListNode(1)
    h1.next = ListNode(2)
    h1.next.next = ListNode(3)
    h1.next.next.next = ListNode(4)
    h1.next.next.next.next = ListNode(5)

    print("h1 list:")
    displaySLL(h1)
    head = Solution().reverseKGroup(h1, 4)
    print("reverseKGroup: ")
    displaySLL(head)

