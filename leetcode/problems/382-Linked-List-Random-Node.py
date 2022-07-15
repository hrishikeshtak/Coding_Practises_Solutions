from random import randint


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:

    def __init__(self, head: Optional[ListNode]):
        self.head = head
        if head is None:
            return head
        self.length = 0
        cur = head
        while cur:
            self.length += 1
            cur = cur.next

    def getRandom(self) -> int:
        rand_index = randint(1, self.length)
        cur = self.head
        cnt = 0
        while cnt < rand_index-1:
            cur = cur.next
            cnt += 1
        return cur.val
