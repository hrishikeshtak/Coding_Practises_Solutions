"""
74. Search a 2D Matrix

Write an efficient algorithm that searches for a value target in an m x n integer matrix matrix.
This matrix has the following properties:

1. Integers in each row are sorted from left to right.
2. The first integer of each row is greater than the last integer of the previous row.

Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
Output: true
"""

from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix:
            return False

        for nums in matrix:
            if target == nums[0] or target == nums[-1]:
                return True
            if target > nums[-1]:
                continue
            elif target > nums[0] and target < nums[-1]:
                return self.binary_search(nums, target)
        return False

    def binary_search(self, nums: List[int], target: int) -> bool:
        if not nums:
            return False

        lo, hi = 0, len(nums) - 1
        while lo <= hi:
            mid = (lo + hi) // 2
            if nums[mid] == target:
                return True
            if target > nums[mid]:
                lo = mid + 1
            else:
                hi = mid - 1
        return False


matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target = 3
print(Solution().searchMatrix(matrix, target))
