#!/usr/bin/python3

"""
Convert Binary Number in a Linked List to Integer

Given head which is a reference node to a singly-linked list. The value of each node in the linked list is either 0 or 1
The linked list holds the binary representation of a number.
Return the decimal value of the number in the linked list.

"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        length = self.size(head) - 1
        print(f"length of linked list: {length}")

        decimal_value = 0
        cur = head
        while cur:
            decimal_value += cur.val * (1 << length)
            cur = cur.next
            length -= 1

        return decimal_value

    def size(self, head: ListNode) -> int:
        if head is None:
            return 0

        size = 0
        cur = head
        while cur:
            size += 1
            cur = cur.next

        return size

    def display(self, head: ListNode):
        if head is None:
            return None

        print("Given Linked List: ")

        cur = head
        while cur:
            if cur.next:
                print(f"{cur.val} -> ", end=" ")
            else:
                print(f"{cur.val}")
            cur = cur.next


if __name__ == '__main__':
    head = ListNode(1)
    head.next = ListNode(0)
    head.next.next = ListNode(1)


    SLL = Solution()
    SLL.display(head)
    decimal_value = SLL.getDecimalValue(head)
    print(f"Decimal value for the given Linked List: {decimal_value}")
