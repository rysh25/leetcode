class Solution:
    def minimumCoins(self, prices: list[int]) -> int:
        n = len(prices)
        dp = [0] * n
        for i in range(n - 1, -1, -1):
            if n > i + i + 2:
                mn = 10**9 + 1
                for j in range(i + 1, i + i + 3):
                    mn = min(mn, dp[j])
                dp[i] = mn
            dp[i] += prices[i]

        # print(f"dp={dp}")

        return dp[0]


sol = Solution()
print(sol.minimumCoins(prices=[3, 1, 2]))
print(sol.minimumCoins(prices=[1, 10, 1, 1]))
