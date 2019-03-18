#!/usr/bin/python3

"""
 Insert Node at the end of a linked list
 head pointer input could be None as well for empty list
 Node is defined as

 class Node(object):

   def __init__(self, data=None, next_node=None):
       self.data = data
       self.next = next_node

 return back the head of the linked list in the below method
"""


def Insert(head, data):
    node = Node(data)
    if not head:
        head = node
    else:
        current = head
        while current.next:
            current = current.next
        current.next = Node(data)
    return(head)
