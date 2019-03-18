#!/usr/bin/python3

# Sample Input

# 1 -> 1 -> 3 -> 3 -> 5 -> 6 -> NULL
# NULL
# Sample Output

# 1 -> 3 -> 5 -> 6 -> NULL
# NULL

"""
 Delete duplicate nodes
 head could be None as well for empty list
 Node is defined as

 class Node(object):

   def __init__(self, data=None, next_node=None):
       self.data = data
       self.next = next_node

 return back the head of the linked list in the below method.
"""


def RemoveDuplicates(head):
    if not head:
        return head

    current = head
    while current.next:
        if current.data == current.next.data:
            current.next = current.next.next
        else:
            current = current.next
    return head
