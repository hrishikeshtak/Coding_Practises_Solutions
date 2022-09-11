"""
239. Sliding Window Maximum
"""

from typing import List

from collections import deque


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # store index in Q - easy to slide windows
        q = deque()
        res = []
        l,  r = 0, 0
        while r < len(nums):
            while q and nums[q[-1]] < nums[r]:
                q.pop()
            q.append(r)
            # pop from left, if windows slides
            if l > q[0]:
                q.popleft()
            if (r + 1) >= k:
                res.append(nums[q[0]])
                l += 1
            r += 1
        return res
