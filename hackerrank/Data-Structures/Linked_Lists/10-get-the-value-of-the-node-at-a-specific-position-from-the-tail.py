#!/usr/bin/python3

# Sample Input

# 1 -> 3 -> 5 -> 6 -> NULL, positionFromTail = 0
# 1 -> 3 -> 5 -> 6 -> NULL, positionFromTail = 2
# Sample Output

# 6
# 3

# Body
"""
 Get Node data of the Nth Node from the end.
 head could be None as well for empty list
 Node is defined as

 class Node(object):

   def __init__(self, data=None, next_node=None):
       self.data = data
       self.next = next_node

 return back the node data of the linked list in the below method.
"""


def GetNode(head, position):
    trailingNode = head
    length = 0
    while head:
        if length > position:
            trailingNode = trailingNode.next

        length += 1
        head = head.next
    return trailingNode.data
