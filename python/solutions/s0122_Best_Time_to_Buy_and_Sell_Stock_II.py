from typing import List


class Solution:
    """
    122. Best Time to Buy and Sell Stock II.

    :see https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/
    """

    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) < 2:
            return 0
        profit = 0
        for i in range(1, len(prices)):
            profit += max(0, prices[i] - prices[i - 1])
        return profit

    # def maxProfit(self, prices: List[int]) -> int:
    #     if len(prices) < 2:
    #         return 0
    #     to_buy = prices[0]
    #     day, limit = 1, len(prices) - 1
    #     while day <= limit:
    #         if prices[day] < to_buy:
    #             to_buy = prices[day]
    #         elif to_buy < prices[day] and (day == limit or prices[day] > prices[day + 1]):
    #             return prices[day] - to_buy + self.maxProfit(prices[day + 1:])
    #         day += 1
    #
    #     return 0
