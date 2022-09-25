"""
11. Container With Most Water

You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.
"""

from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        # # Brute Force O(n*)
        # area = 0
        # res = 0
        # n = len(height)
        # for i in range(n):
        #     for j in range(i+1, n):
        #         area = min(height[i], height[j]) * (j-i)
        #         res = max(area, res)
        # return res

        # Optimize Solution O(n)
        area = 0
        left = 0
        right = len(height) - 1

        while left < right:
            min_height = min(height[left], height[right])
            area = max(area, min_height * (right - left))

            if height[left] <= height[right]:
                left += 1
            else:
                right -= 1
        return area


height = [1,8,6,2,5,4,8,3,7]
print(f"maxArea: {Solution().maxArea(height)}")
