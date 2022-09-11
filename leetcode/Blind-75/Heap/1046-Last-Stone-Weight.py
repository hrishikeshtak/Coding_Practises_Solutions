"""
1046. Last Stone Weight
"""

import heapq
from typing import List


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # prepare max Heap and take 2 largest element
        # to convert array into max heap convert each number to -ve number
        stones = [-s for s in stones]
        # stones = [-2, -7, -4, -1, -8, -1]
        heapq.heapify(stones)
        
        while len(stones) > 1:
            first = heapq.heappop(stones)  # -8
            second = heapq.heappop(stones)  # -7
            
            if second > first:
                heapq.heappush(stones, first - second)
        # if stones array empty
        stones.append(0)
        return abs(stones[0])
        
