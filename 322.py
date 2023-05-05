from typing import List


# https://leetcode.com/problems/coin-change/
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [10**18] * (amount + 1)

        dp[0] = 0
        for a in range(1, amount + 1):
            for c in coins:
                if a >= c:
                    dp[a] = min(dp[a - c] + 1, dp[a])
        return -1 if dp[amount] == 10**18 else dp[amount]


sol = Solution()
print(sol.coinChange(coins=[2], amount=3))
