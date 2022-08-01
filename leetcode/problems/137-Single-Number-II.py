"""
137. Single Number II

Given an integer array nums where every element appears three times except for one, which appears exactly once.
Find the single element and return it.

You must implement a solution with a linear runtime complexity and use only constant extra space.
"""

from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ans = 0
        for i in range(0, 32):
            cnt = 0
            for j in nums:
                if self.checkBit(j, i):
                    cnt += 1
            if cnt % 3 != 0:
                ans = ans | (1 << i)
        return ans - 2**32 if ans >> 31 & 1 else ans
    
    def checkBit(self, i, j):
        return (i >> j) & 1


# nums = [0,1,0,1,0,1,99]
# print(Solution().singleNumber(nums))
nums = [-2,-2,1,1,4,1,4,4,-4,-2]
print(Solution().singleNumber(nums))
