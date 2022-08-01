"""
42. Trapping Rain Water

Given n non-negative integers representing an elevation map where the width of each bar is 1,
compute how much water it can trap after raining.


Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.
"""

from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        # 1. Brute Force O(n*n)
#         count = 0
#         left_max = -(1<<31)
        
#         for i in range(len(height)):
#             right_max = height[i]
#             left_max = max(left_max, height[i])
#             for j in range(i+1, len(height)):
#                 right_max = max(right_max, height[j])
#             count += min(left_max, right_max) - height[i]
#         return count

        # 2. Optimal Time: O(n) Space: O(n)
#         n = len(height)
#         max_left = [0] * n
#         max_right = [0] * n
#         ans = 0
        
#         max_left[0] = height[0]
#         for i in range(1, n):
#             max_left[i] = max(max_left[i-1], height[i])
        
#         max_right[n-1] = height[n-1]
#         for i in range(n-2, -1, -1):
#             max_right[i] = max(max_right[i+1], height[i])
        
#         for i in range(n):
#             ans += min(max_left[i], max_right[i]) - height[i]
#         return ans
        
        # 3. two pointer Time: O(n)
        if not height:
            return 0
        
        l, r = 0, len(height) -1
        maxLeft = height[l]
        maxRight = height[r]
        
        res = 0
        while l < r:
            if maxLeft <= maxRight:
                l += 1
                maxLeft = max(maxLeft, height[l])
                res += maxLeft - height[l]
            else:
                r -= 1
                maxRight = max(maxRight, height[r])
                res += maxRight - height[r]
        return res
        

height = [0,1,0,2,1,0,1,3,2,1,2,1]
print(f"trap: {Solution().trap(height)}")
