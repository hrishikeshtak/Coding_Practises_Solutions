"""
739. Daily Temperatures
"""

from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # similar to find 1st larger element on right side
        stack = []  # store indexes
        n = len(temperatures)
        ans = [0] * n
        for i in range(n-1, -1, -1):
            while stack and temperatures[i] >= temperatures[stack[-1]]:
                _ = stack.pop()
            if stack:
                ans[i] = stack[-1] - i
            stack.append(i)
        return ans
