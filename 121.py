from typing import List


class Solution_sw:
    def maxProfit(self, prices: List[int]) -> int:
        right = 0
        left = 0
        profit = 0
        while right < len(prices):
            if prices[left] > prices[right]:
                left = right
            profit = max(profit, prices[right] - prices[left])
            right += 1
        return profit


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lowest = 10**18
        profit = 0
        for price in prices:
            lowest = min(lowest, price)
            profit = max(profit, price - lowest)

        return profit


sol = Solution()
print(sol.maxProfit(prices=[7, 1, 5, 3, 6, 4]))
print(sol.maxProfit(prices=[7, 6, 4, 3, 1]))
print(sol.maxProfit(prices=[]))
