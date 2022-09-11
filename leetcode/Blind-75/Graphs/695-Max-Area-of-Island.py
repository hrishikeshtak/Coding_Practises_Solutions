"""
695. Max Area of Island
"""

from typing import List


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0

        rows, cols = len(grid), len(grid[0])
        q = []
        visited = set()
        island = 0

        dirs = [[0, -1], [0, 1], [-1, 0], [1, 0]]
        ans = 0

        def bfs(i, j):
            q.append((i, j))
            visited.add((i, j))
            area = 1
            while q:
                r, c = q.pop(0)
                for dr, dc in dirs:
                    row, col = r + dr, c + dc
                    if row in range(rows) and \
                       col in range(cols) and \
                       grid[row][col] == 1 and \
                       (row, col) not in visited:
                        area += 1
                        q.append((row, col))
                        visited.add((row, col))
            return area

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1 and ((i, j) not in visited):
                    island += 1
                    area = bfs(i, j)
                    ans = max(ans, area)
        # print(f"island: {island}")
        return ans
