"""
122. Best Time to Buy and Sell Stock II
"""

from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        red = prices[0]  # down
        blue = prices[0]  # up
        i = 0
        max_profit = 0
        n = len(prices) - 1
        while i < n:
            while i < n and prices[i] >= prices[i+1]:
                i += 1

            down = prices[i]  # update down

            while i < n and prices[i] <= prices[i+1]:
                i += 1
            up = prices[i]  # update up
            max_profit += up - down
        return max_profit
