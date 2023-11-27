class Solution:
    def knightDialer(self, n: int) -> int:
        """
        チェスの騎士と電話パッドがあります。騎士は数字のセルの上にのみ立つことができます。
        整数 n を指定すると、ダイヤルできる長さ n の異なる電話番号の数を返します。

        - Time complexity: O(n)
        - Space complexity: O(n)

        #DP

        Args:
            n (int): 整数

        Returns:
            int: ダイヤルできる長さ n の異なる電話番号の数を返します。
        """
        MOD = 10**9 + 7
        d: list[list[int]] = [[] for _ in range(10)]
        d[0] += [4, 6]
        d[1] += [6, 8]
        d[2] += [7, 9]
        d[3] += [4, 8]
        d[4] += [0, 3, 9]
        d[6] += [0, 1, 7]
        d[7] += [2, 6]
        d[8] += [1, 3]
        d[9] += [2, 4]

        dp: list[list[int]] = [[0] * n for _ in range(10)]
        for i in range(10):
            dp[i][0] = 1

        for j in range(1, n):
            for i in range(10):
                for k in d[i]:
                    # print(f"i={i}, j-1={j-1}, dp[k][j - 1]={dp[k][j - 1]}")
                    dp[i][j] += dp[k][j - 1] % MOD
                # print(f"dp[i][j]={dp[i][j]}")
        # print(f"dp={dp}")

        ans = 0
        for i in range(10):
            ans += dp[i][n - 1] % MOD
        return ans % MOD


sol = Solution()
print(sol.knightDialer(n=1))
print(sol.knightDialer(n=2))
print(sol.knightDialer(n=5))
print(sol.knightDialer(n=3131))
