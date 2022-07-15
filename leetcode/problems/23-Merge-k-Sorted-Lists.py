"""
23. Merge k Sorted Lists
You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.

Merge all the linked-lists into one sorted linked-list and return it.

Input: lists = [[1,4,5],[1,3,4],[2,6]]
Output: [1,1,2,3,4,4,5,6]
Explanation: The linked-lists are:
[
  1->4->5,
  1->3->4,
  2->6
]
merging them into one sorted list:
1->1->2->3->4->4->5->6
"""

from typing import List, Optional
from queue import PriorityQueue


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

        
class Solution1:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # Time: O(n*k)
        if not lists:
            return None

        k = len(lists)
        if k == 1:
            return lists[0]

        # merge first two sorted lists
        if k >= 2:
            head = self.merge2Lists(lists[0], lists[1])
            # print("merge2Lists")
            # displaySLL(head)

        for i in range(2, k):
            head = self.merge2Lists(head, lists[i])
            # print("merge2Lists")
            # displaySLL(head)

        return head

    def merge2Lists(self, head1: ListNode, head2: ListNode) -> ListNode:
        # Time: O(n)
        if not head1 and head2:
            return head2
        elif head1 and not head2:
            return head1
        elif not head1 and not head2:
            return None

        dummy = ListNode(-1)
        c_dummy = dummy

        cur1 = head1
        cur2 = head2

        while cur1 and cur2:
            if cur1.val <= cur2.val:
                temp = ListNode(cur1.val)
                dummy.next = temp
                cur1 = cur1.next
            else:
                temp = ListNode(cur2.val)
                dummy.next = temp
                cur2 = cur2.next
            dummy = dummy.next

        if cur1:
            dummy.next = cur1
        if cur2:
            dummy.next = cur2

        return c_dummy.next


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # using PriorityQueue
        q = PriorityQueue()

        dummy = c_dummy = ListNode(0)

        for l in lists:
            if l:
                q.put((l.val, l))

        # print(f"queue: {q}")

        while not q.empty():
            val, node = q.get()
            print(val, node)
            dummy.next = ListNode(val)
            dummy = dummy.next
            node = node.next
            if node:
                q.put((node.val, node))
        return c_dummy.next


def displaySLL(l1: Optional[ListNode]):
    cur = l1
    while cur:
        print(cur.val, end=" ")
        cur = cur.next
    print()


if __name__ == "__main__":
    # lst = [[1,4,5],[1,3,4],[2,6]]
    h1 = ListNode(1)
    h1.next = ListNode(4)
    h1.next.next = ListNode(5)

    h2 = ListNode(1)
    h2.next = ListNode(3)
    h2.next.next = ListNode(4)

    h3 = ListNode(2)
    h3.next = ListNode(6)

    print("h1 list:")
    displaySLL(h1)
    print("h2 list:")
    displaySLL(h2)
    print("h3 list:")
    displaySLL(h3)
    head = Solution().mergeKLists([h1, h2, h3])
    # head = Solution().mergeKLists([[], h2, h3])
    print("mergeKLists: ")
    displaySLL(head)
