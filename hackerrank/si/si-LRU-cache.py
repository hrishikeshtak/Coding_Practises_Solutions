#!/usr/bin/python3


# LRU Cache implementation using DLL + Hashmap
# LRU -> x -> y -> MRU
class DLL:
    def __init__(self, key):
        self.val = key
        self.next = None
        self.prev = None


def Node(pageNumber):
    node = DLL(pageNumber)
    return node


def LRU_cache(arr, K):
    # hashmap to store address of node
    hashmap = dict()
    # create dummy node
    h = Node(-1)
    t = h
    count = 0  # to check cache is full or not

    N = len(arr)
    for i in range(0, N):
        displayDLL(h)
        print(hashmap)
        # if page found in cache
        if arr[i] in hashmap:
            # remove that page from DLL and add in the end (MRU)
            temp = hashmap[arr[i]]
            # remove from DLL
            temp.prev.next = temp.next
            temp.next.prev = temp.prev

            # append in the DLL (MRU)
            t.next = temp
            temp.prev = t
            t = temp
            temp.next = None
        else:
            newnode = Node(arr[i])
            # add page -> address in hashmap
            hashmap[arr[i]] = newnode
            # if cache is full, then remove head node (LRU)
            if count == K:
                val = h.next.val
                h.next = h.next.next
                h.next.prev = h
                count -= 1
                # remove LRU node from hashmap
                hashmap.pop(val)
            # add new node at the end of DLL (MRU)
            newnode.prev = t
            t.next = newnode
            t = newnode
            count += 1
    displayDLL(h)
    print(hashmap)


def displayDLL(head):
    cur = head
    while cur:
        print(cur.val, end=" ")
        cur = cur.next


def main():
    arr = list(map(int, input().split()))
    cache_size = int(input())
    LRU_cache(arr, cache_size)


if __name__ == '__main__':
    main()
