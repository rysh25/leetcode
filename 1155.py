class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        """
        n 個のサイコロがあり、それぞれのサイコロには 1 から k までの番号が付けられた k 個の面があります。

        3 つの整数 n、k、target を指定すると、表向きの数字の合計が target と等しくなるように、
        (k^n 個の合計方法のうち) サイコロを振る可能な方法の数を返します。
        答えが大きすぎる可能性があるため、10^9 + 7 を法にして返します。

        - Time complexity: O(target * n * k)
        - Space complexity: O(target * n)

        #DP

        Args:
            n (int): サイコロの個数
            k (int): サイコロにk 個の面があることを表す。
            target (int): 表向きの数字の合計を target と等しくする。

        Returns:
            int: サイコロを振る可能な方法の数を返します。
        """
        MOD = 10**9 + 7
        dp: list[list[int]] = [[0] * (target + 1) for _ in range(n)]
        for j in range(1, target + 1):
            if j > k:
                break
            dp[0][j] = 1

        # print(f"n={n}, k={k}, target={target}, dp={dp}")

        for i in range(1, n):
            for j in range(1, target):
                sum = 0
                for l in range(k):
                    if j - l >= 0 and j - l < target:
                        sum += dp[i - 1][j - l] % MOD
                dp[i][j + 1] = sum % MOD
                # print(f"i={i}, j={j}, dp={dp}")

        # print(f"dp={dp}")
        return dp[n - 1][target]


sol = Solution()
print(sol.numRollsToTarget(n=1, k=6, target=3))
print(sol.numRollsToTarget(n=2, k=6, target=7))
print(sol.numRollsToTarget(n=4, k=6, target=8))
print(sol.numRollsToTarget(n=3, k=6, target=14))
print(sol.numRollsToTarget(n=30, k=30, target=500))
