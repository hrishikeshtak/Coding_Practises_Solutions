"""
167. Two Sum II - Input Array Is Sorted

Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order,
find two numbers such that they add up to a specific target number.
Let these two numbers be numbers[index1] and numbers[index2] where 1 <= index1 < index2 <= numbers.length.
"""

from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        lo, hi = 0, len(numbers) - 1

        ans = []
        while lo < hi:
            _sum = numbers[lo] + numbers[hi]
            if _sum == target:
                return [lo + 1, hi + 1]
            elif _sum > target:
                hi = hi - 1
            else:
                lo = lo + 1


if __name__ == '__main__':
    numbers = [2,7,11,15]
    target = 9
    print(Solution().twoSum(numbers, target))
