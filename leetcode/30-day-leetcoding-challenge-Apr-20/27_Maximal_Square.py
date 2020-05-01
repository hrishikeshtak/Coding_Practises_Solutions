#!/usr/bin/python3

"""
Maximal Square
Given a 2D binary matrix filled with 0's and 1's, find the largest square containing only 1's and return its area.

Input:

1 0 1 0 0
1 0 1 1 1
1 1 1 1 1
1 0 0 1 0

Output: 4
"""


class Solution:
    def maximalSquare(self, matrix: 'List[List[str]]') -> int:

        if not matrix:
            return 0

        m = len(matrix)
        n = len(matrix[0])

        dp = [[None] * (n+1) for i in range(m+1)]

        res = 0

        for i in range(m+1):
            for j in range(n+1):
                if i == 0 or j == 0:
                    dp[i][j] = 0
                elif matrix[i-1][j-1] == '1':
                    dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
                    res = max(res, dp[i][j])
                else:
                    dp[i][j] = 0

        return res * res


if __name__ == '__main__':
    # matrix = [['1', '0', '1', '0', '0'],
    #           ['1', '0', '1', '1', '1'],
    #           ['1', '1', '1', '1', '1'],
    #           ['1', '0', '0', '1', '1']]
    matrix = []
    matrix = [["1","0","1","0"],["1","0","1","1"],["1","0","1","1"],["1","1","1","1"]]
    print(f"{Solution().maximalSquare(matrix)}")
