"""
70. Climbing Stairs
"""

class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 3:
            return n
        one, two = 1, 1
        for i in range(n-1):
            temp = one
            one = one + two
            two = temp
        return one

#         # DP - Bottom Up
#         dp = [0] * (n+1)
#         dp[n] = 1  # to reach nth step from n step
#         dp[n-1] = 1  # to reach nth step from n-1 step        
#         for i in range(n-2, -1, -1):
#             dp[i] = dp[i+1] + dp[i+2]
#         return dp[0]
