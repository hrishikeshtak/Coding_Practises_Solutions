#!/usr/bin/python3

"""
 Insert a node into a sorted doubly linked list
 head could be None as well for empty list
 Node is defined as

 class Node(object):

   def __init__(self, data=None, next_node=None, prev_node = None):
       self.data = data
       self.next = next_node
       self.prev = prev_node

 return the head node of the updated list
"""


def SortedInsert(head, data):
    node = Node(data, None, None)
    if head is None:
        return node
    elif data < head.data:
        node.next = head
        head.prev = node
        return node
    else:
        node = SortedInsert(head.next, data)
        head.next = node
        node.prev = head
        return head
