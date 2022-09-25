"""
53. Maximum Subarray
"""

from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        _sum = 0
        max_sum = 0
        for i in range(len(nums)):
            if _sum + nums[i] < 0:
                _sum = 0
            else:
                _sum += nums[i]
            max_sum = max(max_sum, _sum)
        
        # if all are negative nums
        if max_sum == 0 and 0 not in nums:
            return max(nums)
        return max_sum
