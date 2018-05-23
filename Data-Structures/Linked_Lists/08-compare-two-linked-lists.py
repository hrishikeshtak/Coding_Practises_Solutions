#!/usr/bin/python3

"""
 Compare two linked list
 head could be None as well for empty list
 Node is defined as

 class Node(object):

   def __init__(self, data=None, next_node=None):
       self.data = data
       self.next = next_node

 return back 1 if equal else 0.
"""


def CompareLists(headA, headB):
    # recursive
    if not headA and not headB:
        return 1
    elif (headA and headB) and (headA.data == headB.data):
        return CompareLists(headA.next, headB.next)
    else:
        return 0


def CompareLists(headA, headB):
    # iterative
    curA = headA
    curB = headB

    while True:
        if not curA and not curB:
            return 1
        elif (curA and curB) and (curA.data == curB.data):
            curA = curA.next
            curB = curB.next
        else:
            return 0
