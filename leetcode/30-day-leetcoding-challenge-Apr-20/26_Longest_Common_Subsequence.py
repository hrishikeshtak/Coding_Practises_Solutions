#!/usr/bin/python3

"""
Longest Common Subsequence
"""


class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:

        m = len(text1)
        n = len(text2)

        dp = [[None] * (n+1) for i in range(m+1)]

        for i in range(m+1):
            for j in range(n+1):
                if i == 0 or j == 0:
                    dp[i][j] = 0
                elif text1[i-1] == text2[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        return dp[i][j]


if __name__ == '__main__':
    S1 = 'AGGTAB'
    S2 = 'GXTXAYB'

    print(f"{Solution().longestCommonSubsequence(S1, S2)}")
