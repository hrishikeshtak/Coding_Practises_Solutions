#!/usr/bin/python3

"""
LRU Cache
DLL + HashMap
"""


class DLLNode:
    def __init__(self, val):
        self.val = val
        self.prev = None
        self.next = None


def NewNode(val):
    return DLLNode(val)


class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        # key: (value, address)
        self.hashmap = {}
        self.tail = NewNode(-1)
        self.head = self.tail
        self.count = 0

    def get(self, key: int) -> int:
        if key in self.hashmap:
            # get address of node
            temp = self.hashmap[key][1]
            # append node at end (MRU)
            if temp.next:
                temp.prev.next = temp.next
                temp.next.prev = temp.prev
                # append at the end (MRU)
                self.tail.next = temp
                temp.prev = self.tail
            self.tail = temp
            self.tail.next = None
            return self.hashmap[key][0]
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.hashmap:
            temp = self.hashmap[key][1]
            # update value
            # remove from hashmap
            _ = self.hashmap.pop(key)
            self.hashmap[key] = (value, temp)
            if temp.next:
                temp.prev.next = temp.next
                temp.next.prev = temp.prev

                # append at the end (MRU)
                self.tail.next = temp
                temp.prev = self.tail
            # update tail
            self.tail = temp
            self.tail.next = None
        else:
            node = NewNode(key)
            self.hashmap[key] = (value, node)

            if self.count == self.capacity:
                # cache full remove LRU node from front
                val = self.head.next.val
                self.head.next = self.head.next.next
                if self.head.next:
                    self.head.next.prev = self.head
                else:
                    self.head = self.tail
                # remove from hashmap
                _ = self.hashmap.pop(val)
                self.count -= 1

            node.prev = self.tail
            self.tail.next = node
            self.tail = node
            self.count += 1


if __name__ == '__main__':
    # Your LRUCache object will be instantiated and called as such:
    # obj = LRUCache(2)
    # obj.put(1, 1)
    # obj.put(2, 2)
    # print(f"{obj.get(1)}")
    # obj.put(3, 3)
    # print(f"{obj.get(2)}")
    # obj.put(4, 4)
    # print(f"{obj.get(1)}")
    # print(f"{obj.get(3)}")
    # print(f"{obj.get(4)}")

    # obj = LRUCache(1)
    # obj.put(2, 1)
    # print(f"{obj.get(2)}")

    # obj = LRUCache(1)
    # obj.put(2, 1)
    # print(f"{obj.get(2)}")
    # obj.put(3, 2)
    # print(f"{obj.get(2)}")
    # print(f"{obj.get(3)}")

    obj = LRUCache(2)
    obj.put(2, 1)
    obj.put(2, 2)
    print(f"{obj.get(2)}")
    obj.put(1, 1)
    obj.put(4, 1)
    print(f"{obj.get(2)}")
