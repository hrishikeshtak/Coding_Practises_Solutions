"""
215. Kth Largest Element in an Array
"""

from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        k = len(nums) - k

        def quickSelect(l, r):
            pivot = nums[r]
            p = l

            for i in range(l, r):
                if nums[i] <= pivot:
                    nums[p], nums[i] = nums[i], nums[p]
                    p += 1
            nums[r] = nums[p]
            nums[p] = pivot

            if k == p:
                return nums[p]
            elif k < p:
                return quickSelect(l, p-1)
            return quickSelect(p+1, r)
        return quickSelect(0, len(nums) - 1)

    def findKthSmallest(self, nums: List[int], k: int) -> int:
        k = k - 1
        def quickSelect(l, r):
            pivot = nums[r]
            p = l

            for i in range(l, r):
                if nums[i] <= pivot:
                    nums[p], nums[i] = nums[i], nums[p]
                    p += 1
            nums[r] = nums[p]
            nums[p] = pivot

            if k == p:
                return nums[p]
            elif k < p:
                return quickSelect(l, p-1)
            return quickSelect(p+1, r)
        return quickSelect(0, len(nums) - 1)


nums = [1, 23, 12, 9, 30, 2, 50]
k = 3
res = Solution().findKthLargest(nums, k)
print(f"findKthLargest: {res}")
res = Solution().findKthSmallest(nums, k)
print(f"findKthSmallest: {res}")
