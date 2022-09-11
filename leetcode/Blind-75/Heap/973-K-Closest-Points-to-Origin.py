"""
973. K Closest Points to Origin
"""

import heapq
from typing import List


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        pts = []
        for x, y in points:
            dist = abs(x**2) + abs(y**2)
            pts.append([dist, x, y])
        
        # Min heap of dist
        heapq.heapify(pts)
        res = []
        while k >= 1:
            dist, x, y = heapq.heappop(pts)
            res.append([x, y])
            k -= 1
        return res
