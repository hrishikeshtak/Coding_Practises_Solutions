"""
84. Largest Rectangle in Histogram
"""

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # # Brute Force: O(n*n)
        # area = float("-infinity")
        # n = len(heights)
        # for i in range(0, n):
        #     min_height = heights[i]
        #     for j in range(i, n):
        #         min_height = min(min_height, heights[j])
        #         area = max(area, ((j - i + 1) * min_height))
        #         # print(f"area: {area}")
        # return area
        area = float("-infinity")
        n = len(heights)
        # find smaller element on left for each element
        left_smaller = [-1] * n
        stack = []
        for i in range(0, n):
            # store indexes
            while stack and heights[i] <= heights[stack[-1]]:
                _ = stack.pop()
            if stack:
                left_smaller[i] = stack[-1]
            stack.append(i)
        # print(f"left_smaller: {left_smaller}")
        # find smaller element on right side for each element
        right_smaller = [n] * n
        stack = []
        for i in range(n-1, -1, -1):
            # store indexes
            while stack and heights[i] <= heights[stack[-1]]:
                _ = stack.pop()
            if stack:
                right_smaller[i] = stack[-1]
            stack.append(i)
        # print(f"right_smaller: {right_smaller}")
        for i in range(0, n):
            area = max(area, ((right_smaller[i] - left_smaller[i] - 1) * heights[i]))
        return area
        
        
                
        