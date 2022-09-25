"""
56. Merge Intervals
"""

from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return None
        # sort the list based on the start
        intervals.sort(key=lambda x: x[0])
        res = [[float("inf"), float("-inf")]]
        j = 0  # res idx
        for i in range(len(intervals)):
            if intervals[i][0] <= res[j][1]:
                # overlap
                res[j] = [
                    min(res[j][0], intervals[i][0]),
                    max(res[j][1], intervals[i][1]),
                ]
            else:
                res.append(intervals[i])
                j += 1
        # print(res[1:])
        return res[1:]
