"""
33. Search in Rotated Sorted Array

Given the array nums after the possible rotation and an integer target,
return the index of target if it is in nums, or -1 if it is not in nums.

You must write an algorithm with O(log n) runtime complexity.

Example 1:

Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4
Example 2:

Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1
"""

from typing import List


class Solution:
    # def search(self, nums: List[int], target: int) -> int:
    #     if not nums:
    #         return -1
    #     lo, hi = 0, len(nums) - 1
    #     pivot = self.findPivot(nums, lo, hi)
    #     if target == nums[pivot]:
    #         return pivot
    #     if target >= nums[lo]:
    #         return self.BSR(nums, lo, pivot, target)
    #     return self.BSR(nums, pivot+1, hi, target)

    def BSR(self, nums, lo, hi, target):
        if hi < lo:
            return -1
        mid = (lo + hi) // 2
        if nums[mid] == target:
            return mid
        if target < nums[mid]:
            return self.BSR(nums, lo, mid-1, target)
        return self.BSR(nums, mid+1, hi, target)

    def findPivot(self, nums, lo, hi):
        if hi < lo:
            return -1
        if lo == hi:
            return lo
        mid = (lo + hi) // 2
        if mid < hi and nums[mid] > nums[mid+1]:
            return mid
        if mid > lo and nums[mid] < nums[mid-1]:
            return mid-1

        if nums[mid] >= nums[lo]:
            return self.findPivot(nums, mid+1, hi)
        return self.findPivot(nums, lo, mid-1)

    def search(self, nums: List[int], target: int) -> int:
        lo, hi = 0, len(nums) - 1

        while lo <= hi:
            mid = (lo + hi) // 2
            if nums[mid] == target:
                return mid

            # mid exist in Left side
            if nums[mid] >= nums[lo]:
                if target > nums[mid]:
                    lo = mid+1
                elif target < nums[lo]:
                    lo = mid+1
                else:
                    hi = mid-1
            else:  # mid exists in right side
                if target < nums[mid]:
                    hi = mid - 1
                elif target > nums[hi]:
                    hi = mid - 1
                else:
                    lo = mid + 1
        return -1


nums = [4,5,6,7,0,1,2]
print(f"nums: {nums}")
print(Solution().search(nums, 0))
