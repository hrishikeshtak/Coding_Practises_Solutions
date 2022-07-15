"""
56. Merge Intervals

Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.

 

Example 1:

Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].
Example 2:

Input: intervals = [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.
"""

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals or not intervals[0]:
            return []
        # sort the intervals array based on start
        intervals.sort(key=lambda x: x[0])
        
        merged = []
        merged.append(intervals[0])
        merged_idx = 0
        for idx in range(1, len(intervals)):
            if intervals[idx][0] <= merged[merged_idx][-1]:
                merged[merged_idx][-1] = max(merged[merged_idx][-1], intervals[idx][-1])
            else:
                merged.append(intervals[idx])
                merged_idx += 1
        return merged
        # Time: O(nlogn)
        # Space: O(n)
