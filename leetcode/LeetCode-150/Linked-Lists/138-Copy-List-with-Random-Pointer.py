"""
138. Copy List with Random Pointer
"""

# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        hashmap = {None: None}
        cur = head
        while cur:
            temp = Node(cur.val)
            hashmap[cur] = temp
            cur = cur.next
        cur = head
        while cur:
            temp = hashmap[cur]
            temp.next = hashmap[cur.next]
            temp.random = hashmap[cur.random]
            cur = cur.next
        return hashmap[head]
