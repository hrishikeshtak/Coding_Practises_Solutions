"""
703. Kth Largest Element in a Stream
"""

import heapq
from typing import List


class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        # minHeap with K element
        self.minHeap = nums
        self.k = k
        heapq.heapify(self.minHeap)
        while len(self.minHeap) > self.k:
            heapq.heappop(self.minHeap)

    def add(self, val: int) -> int:
        heapq.heappush(self.minHeap, val)
        while len(self.minHeap) > self.k:
            heapq.heappop(self.minHeap)
        return self.minHeap[0]


# Your KthLargest object will be instantiated and called as such:
k = 3
nums = [4, 5, 8, 2]
obj = KthLargest(k, nums)
print(f"Kth: {k} Largest: {obj.add(3)}")
print(f"Kth: {k} Largest: {obj.add(5)}")
print(f"Kth: {k} Largest: {obj.add(10)}")
print(f"Kth: {k} Largest: {obj.add(9)}")
print(f"Kth: {k} Largest: {obj.add(4)}")
