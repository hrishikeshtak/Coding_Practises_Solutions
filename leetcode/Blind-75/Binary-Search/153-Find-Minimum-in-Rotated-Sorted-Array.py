"""
153. Find Minimum in Rotated Sorted Array
Given the sorted rotated array nums of unique elements, return the minimum element of this array.

You must write an algorithm that runs in O(log n) time.
Example 1:

Input: nums = [3,4,5,1,2]
Output: 1
Explanation: The original array was [1,2,3,4,5] rotated 3 times.
"""

from typing import List


class Solution:
    def findMax(self, nums: List[int]) -> int:
        lo, hi = 0, len(nums) - 1

        while lo < hi:
            mid = (lo + hi) // 2
            if mid < hi and nums[mid] > nums[mid+1]:
                return nums[mid]
            elif mid > lo and nums[mid] < nums[mid-1]:
                return nums[mid-1]
            if nums[mid] >= nums[lo]:
                lo = mid + 1
            else:
                hi = mid - 1
        if lo == hi:
            return nums[lo]

    def findMin(self, nums: List[int]) -> int:
        res = nums[0]
        lo, hi = 0, len(nums) - 1

        while lo <= hi:
            if nums[lo] <= nums[hi]:
                res = min(res, nums[lo])
                break

            mid = (lo + hi) // 2
            res = min(res, nums[mid])
            if nums[mid] >= nums[lo]:
                lo = mid + 1
            else:
                hi = mid - 1
        return res


nums = [3,4,5,1,2]
nums = [3,4,5,6,7]
nums = [5,1,2,3,4]
print(f"findMax: {Solution().findMax(nums)}")
print(f"findMin: {Solution().findMin(nums)}")