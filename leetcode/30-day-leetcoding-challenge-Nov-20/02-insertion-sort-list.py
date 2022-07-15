#!/usr/bin/python3

"""
Given the head of a singly linked list, sort the list using insertion sort, and return the sorted list's head.
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        # convert SLL to array
        arr = []
        cur = head

        while cur:
            arr.append(cur.val)
            cur = cur.next

        sorted_arr = self.insertionSortArr(arr)

        cur = head
        for val in arr:
            cur.val = val
            cur = cur.next

        return head

    def insertionSortArr(self, arr):
        # print(f"before sorted: {arr}")
        N = len(arr)

        if len(arr) < 2:
            return arr

        for i in range(1, N):
            temp = arr[i]
            # print(f"arr: {arr} temp: {temp}")
            j = i
            while j > 0 and arr[j-1] > temp:
                arr[j] = arr[j-1]
                j -= 1
            arr[j] = temp
        # print(f"after sorted: {arr}")
        return arr

    @staticmethod
    def display(head: ListNode):
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
    obj = Solution()
    head = ListNode(4)
    head.next = ListNode(2)
    head.next.next = ListNode(1)
    head.next.next.next = ListNode(3)
    obj.display(head)
    obj.insertionSortList(head)
    obj.display(head)
