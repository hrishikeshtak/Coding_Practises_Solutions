"""
Best Time to Buy and Sell Stock

You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
"""

from typing import List


class Solution:
    # def maxProfit(self, prices: List[int]) -> int:
    #     n = len(prices)
    #     max_profit = 0

    #     if not prices:
    #         return max_profit

    #     # prepare prefix array from left end with minimum element from the array
    #     left_prefix_array = [prices[0]] * n
    #     # prepare suffix array from right end with maximum element from the array
    #     right_suffix_array = [prices[-1]] * n

    #     for i in range(1, n):
    #         left_prefix_array[i] = min(left_prefix_array[i-1], prices[i])

    #     # print(f"left_prefix_array: {left_prefix_array}")

    #     for i in range(n-2, -1, -1):
    #         right_suffix_array[i] = max(prices[i], right_suffix_array[i+1])

    #     # print(f"right_suffix_array: {right_suffix_array}")

    #     for i in range(0, n):
    #         max_profit = max((right_suffix_array[i] - left_prefix_array[i]), max_profit)

    #     return max_profit

    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        max_profit = 0

        if not prices:
            return max_profit

        buy = prices[0]

        for i in range(1, n):
            if buy > prices[i]:
                buy = prices[i]

            max_profit = max((prices[i] - buy), max_profit)

        return max_profit


if __name__ == '__main__':
    prices = [7,1,5,3,6,4]
    # prices = [7, 6, 4, 3, 1]
    # prices = [2]
    res = Solution().maxProfit(prices)
    print(f"maxProfit: {res}")
