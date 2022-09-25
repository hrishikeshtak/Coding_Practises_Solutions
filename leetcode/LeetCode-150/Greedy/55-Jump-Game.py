"""
55. Jump Game
"""

from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        last_point = n - 1        
        for i in range(n-1, -1, -1):
            if i + nums[i] >= last_point:
                last_point = i
        return last_point == 0
