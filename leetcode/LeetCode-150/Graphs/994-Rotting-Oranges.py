"""
994. Rotting Oranges
"""

from typing import List

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        if not grid:
            return -1
        rows, cols = len(grid), len(grid[0])
        q = []
        
        # find all the rotten oranges and put them into q
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    q.append((r, c))
        q.append(None)

        def bfs():
            ans = 0
            dirs = [[0, -1], [0, 1], [-1, 0], [1, 0]]  # 4 direction
            while len(q) > 1:
                cur = q.pop(0)
                if cur is None:
                    ans += 1
                    q.append(None)
                else:
                    r, c = cur
                    for dr, dc in dirs:
                        row, col = r + dr, c + dc
                        if row in range(rows) and \
                           col in range(cols) and \
                           grid[row][col] == 1:
                            q.append((row, col))
                            grid[row][col] = 2
            return ans
        ans = bfs()
        # check if all the oranges are rotten
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    return -1
        return ans
