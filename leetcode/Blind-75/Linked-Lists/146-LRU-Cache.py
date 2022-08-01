"""
146. LRU Cache
"""


class DLLNode:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {}
        self.capacity = capacity

        self.left, self.right = DLLNode(0, 0), DLLNode(0, 0)
        self.left.next = self.right
        self.right.prev = self.left

    def insert(self, node):
        # insert at right
        # update left ptr
        prev, nxt = self.right.prev, self.right
        prev.next = nxt.prev = node
        node.next = nxt
        node.prev = prev

    def remove(self, node):
        # remove from left
        prev, nxt = node.prev, node.next
        prev.next = nxt
        nxt.prev = prev

    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = DLLNode(key, value)
        self.insert(self.cache[key])

        if len(self.cache) > self.capacity:
            # remove from list and delete from cache
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]



# Your LRUCache object will be instantiated and called as such:
capacity = 2
obj = LRUCache(capacity)
print(f"get 1: {obj.get(1)}")
obj.put(1, 1)
obj.put(2, 2)
print(f"get 1: {obj.get(1)}")
obj.put(3, 3)
print(f"get 1: {obj.get(1)}")
