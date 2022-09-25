"""
45. Jump Game II
"""

from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        # using DFS approach
        res = 0
        l = r = 0
        
        while r < len(nums) - 1:
            farthest = l
            for i in range(l, r+1):
                farthest = max(farthest, i + nums[i])
            l = r + 1
            r = farthest
            res += 1
        return res
