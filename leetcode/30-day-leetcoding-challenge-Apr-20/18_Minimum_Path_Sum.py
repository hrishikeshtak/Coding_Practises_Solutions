#!/usr/bin/python3

"""
Minimum Path Sum

Note: You can only move either down or right at any point in time.
"""


class Solution:
    def minPathSum(self, grid: 'List[List[int]]') -> int:
        if not grid:
            return 0

        R = len(grid)
        C = len(grid[0])
        dp = [[0] * C] * R

        dp[0][0] = grid[0][0]

        for i in range(0, R):
            # print(f"dp: {dp}")
            # for column 0
            if i > 0:
                dp[i][0] = dp[i-1][0] + grid[i][0]
            for j in range(1, C):
                if i == 0:
                    dp[i][j] = dp[i][j-1] + grid[i][j]
                else:
                    dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + grid[i][j]
        # print(f"dp: {dp}")

        return dp[R-1][C-1]


if __name__ == '__main__':
    mat = [
      [1, 3, 2],
      [4, 3, 1],
      [5, 6, 1]
    ]
    print(f"{Solution().minPathSum(mat)}")
