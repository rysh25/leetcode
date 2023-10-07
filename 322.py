class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:
        """
        異なる金種を表す整数の配列 coins と、合計金額を表す整数 amount が与えられる。
        その金額を作る最も少ないコインの枚数を返す。作れない場合 -1 を返す。
        各金種のコインの枚数は無限に持っているとする。

        - Time complexity: O(n * amount)
        - Space complexity: O(n * amount)

        #DP

        Args:
            coins (list[int]): 金種を表す整数の配列
            amount (int): 合計金額

        Returns:
            int: 金額を作る最も少ないコインの枚数を返す。作れない場合 -1 を返す。
        """
        print(f"coint={coins}, amount={amount}")
        INF = 10**9 + 1
        n = len(coins)
        dp: list[list[int]] = [[INF] * (amount + 1) for _ in range(n + 1)]
        dp[0][0] = 0
        for i in range(1, n + 1):
            for j in range(amount + 1):
                if j - coins[i - 1] >= 0:
                    dp[i][j] = min(dp[i][j - coins[i - 1]] + 1, dp[i - 1][j])
                else:
                    dp[i][j] = dp[i - 1][j]

        print(f"dp={dp}")

        return dp[n][amount] if dp[n][amount] < INF else -1


sol = Solution()
print(sol.coinChange(coins=[1, 2, 5], amount=11))
print(sol.coinChange(coins=[2], amount=3))
print(sol.coinChange(coins=[1], amount=0))
print(sol.coinChange(coins=[8, 4], amount=8))
