#!/usr/bin/python3

"""
Best Time to Buy and Sell Stock II
Say you have an array for which the ith element is the price of a given
stock on day i.

Design an algorithm to find the maximum profit.
You may complete as many transactions as you like
(i.e., buy one and sell one share of the stock multiple times).

Note: You may not engage in multiple transactions at the same time
(i.e., you must sell the stock before you buy again).

Input: [7,1,5,3,6,4]
Output: 7
Explanation: Buy on day 2 (price = 1) and sell on day 3 (price = 5), profit = 5-1 = 4.
             Then buy on day 4 (price = 3) and sell on day 5 (price = 6), profit = 6-3 = 3.

"""


class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0

        maxprofit = 0
        valley = prices[0]
        peak = prices[0]

        n = len(prices) - 1
        i = 0

        while i < n:
            while i < n and prices[i] >= prices[i+1]:
                i += 1

            valley = prices[i]

            while i < n and prices[i] <= prices[i+1]:
                i += 1

            peak = prices[i]

            maxprofit += peak - valley

        return maxprofit


if __name__ == '__main__':
    arr = [7, 1, 5, 3, 6, 4]
    print(f"maxProfit = {Solution().maxProfit(arr)}")
    arr = [7, 1, 5, 6, 3, 4]
    print(f"maxProfit = {Solution().maxProfit(arr)}")
    arr = [1, 2, 3, 4, 5]
    print(f"maxProfit = {Solution().maxProfit(arr)}")
    arr = [5, 4, 3, 2, 1]
    print(f"maxProfit = {Solution().maxProfit(arr)}")
    arr = []
    print(f"maxProfit = {Solution().maxProfit(arr)}")
    arr = [1]
    print(f"maxProfit = {Solution().maxProfit(arr)}")