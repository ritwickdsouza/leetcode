# Problem - https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lowest_price = float('inf')
        max_profit = float('-inf')
        for current_price in prices:
            lowest_price = min(lowest_price, current_price)
            current_profit = current_price - lowest_price
            max_profit = max(max_profit, current_profit)
        return max_profit


"""
Runtime: 2332 ms, faster than 5.12% of Python3 online submissions for Best Time to Buy and Sell Stock.
Memory Usage: 25.1 MB, less than 38.07% of Python3 online submissions for Best Time to Buy and Sell Stock.
"""
