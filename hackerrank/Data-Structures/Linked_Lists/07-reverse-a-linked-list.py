#!/usr/bin/python3

"""
 Reverse a linked list
 head could be None as well for empty list
 Node is defined as

 class Node(object):

   def __init__(self, data=None, next_node=None):
       self.data = data
       self.next = next_node

 return back the head of the linked list in the below method.
"""


def Reverse(head):
    if head:
        current_node = head
        next_node = current_node.next
        current_node.next = None
        while next_node:
            tmp = next_node.next
            next_node.next = current_node
            head = current_node = next_node
            next_node = tmp
    return head
