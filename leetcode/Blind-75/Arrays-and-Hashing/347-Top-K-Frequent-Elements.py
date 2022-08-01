"""
347. Top K Frequent Elements

Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.
"""

from collections import Counter
from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)
        cnt = 0
        result = []

        for i, j in sorted(counter.items(), key=lambda x: x[1], reverse=True):
            if cnt < k:
                result.append(i)
                cnt += 1
            else:
                break
        return result


if __name__ == '__main__':
    nums = [1,1,1,2,2,3]
    k = 2
    print(f"topKFrequent: {Solution().topKFrequent(nums, k)}")
