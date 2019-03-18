#!/usr/bin/python3


"""
 Merge two linked lists
 head could be None as well for empty list
 Node is defined as

 class Node(object):

   def __init__(self, data=None, next_node=None):
       self.data = data
       self.next = next_node

 return back the head of the linked list in the below method.
"""

# Sample Input

# 1 -> 3 -> 5 -> 6 -> NULL
# 2 -> 4 -> 7 -> NULL

# 15 -> NULL
# 12 -> NULL

# NULL
# 1 -> 2 -> NULL
# Sample Output

# 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 -> NULL
# 12 -> 15 -> NULL
# 1 -> 2 -> NULL


def MergeLists(headA, headB):
    if not headA:
        return headB
    elif not headB:
        return headA

    if headA.data < headB.data:
        headA.next = MergeLists(headA.next, headB)
        return headA
    else:
        headB.next = MergeLists(headA, headB.next)
        return headB
