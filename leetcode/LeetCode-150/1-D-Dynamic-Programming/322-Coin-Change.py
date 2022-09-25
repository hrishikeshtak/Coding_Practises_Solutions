"""
322. Coin Change
"""

from typing import List

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [amount + 1] * (amount + 1)
        dp[0] = 0 # base case

        # sort the coins array
        # coins.sort()

        for i in range(1, amount+1):
            for c in coins:
                if i - c >= 0:
                    dp[i] = min(dp[i], 1 + dp[i-c])
        return dp[amount] if dp[amount] != amount + 1 else -1
        # Time: O(amount * len(coins))
        # Space: O(amount)
