#!/usr/bin/python3

"""
Middle_of_the_Linked_List
Given a non-empty, singly linked list with head node head,
return a middle node of linked list.

If there are two middle nodes, return the second middle node.
"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
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

    def insertNode(self, head, val):
        cur = head
        if head is None:
            return ListNode(val)

        while cur.next:
            cur = cur.next

        cur.next = ListNode(val)
        return head

    def displayList(self, head):
        cur = head
        while cur:
            print(cur.val, end=' ')
            cur = cur.next
        print()


if __name__ == '__main__':
    head = None
    # breakpoint()
    head = Solution().insertNode(head, 1)
    head = Solution().insertNode(head, 2)
    head = Solution().insertNode(head, 3)
    head = Solution().insertNode(head, 4)
    head = Solution().insertNode(head, 5)
    head = Solution().insertNode(head, 6)

    Solution().displayList(head)

    node = Solution().middleNode(head)
    Solution().displayList(node)
