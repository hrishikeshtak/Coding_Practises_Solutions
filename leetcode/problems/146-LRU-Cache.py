"""
146. LRU Cache
"""

class ListNode:
    def __init__(self, val):
        self.val = val
        self.prev = None
        self.next = None


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.hashmap = {}
        self.count = 0
        self.head = self.tail = ListNode(-1)

    def get(self, key: int) -> int:
        if key in self.hashmap:
            val, node = self.hashmap[key]
            if node.next:
                node.prev.next = node.next
                node.next.prev = node.prev

                # add the node to the tail of DLL - MRU
                self.tail.next = node
                node.prev = self.tail
            self.tail =  node
            self.tail.next = None
            return val
        return -1        

    def put(self, key: int, value: int) -> None:
        if key in self.hashmap:
            # get address of node from hashmap
            _, node = self.hashmap[key]
            # remove key from hashmap and add new (key, value)
            _ = self.hashmap.pop(key)
            self.hashmap[key] = (value, node)
            if node.next:
                node.next.prev = node.prev
                node.prev.next = node.next

                self.tail.next = node
                node.prev = self.tail
            self.tail = node
            self.tail.next = None
        else:
            node = ListNode(key)
            self.hashmap[key] = (value, node)

            # cache capacity is full
            if self.count == self.capacity:
                # remove node from head - LRU
                val = self.head.next.val
                self.head.next = self.head.next.next
                if self.head.next:
                    self.head.next.prev = self.head
                else:
                    self.head = self.tail
                # remove node from hashmap
                _ = self.hashmap.pop(val)
                self.count -= 1

            # add node at the end - MRU
            node.prev = self.tail
            self.tail.next = node
            self.tail = node
            self.count += 1
            


# Your LRUCache object will be instantiated and called as such:
obj = LRUCache(2)
print(obj.get(1))
obj.put(1, 1)
obj.put(2, 2)
print(obj.get(1))
print(obj.get(2))
print(obj.get(3))
obj.put(3, 3)
print(obj.get(3))
print(obj.get(2))
print(obj.get(1))