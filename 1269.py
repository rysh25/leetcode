class Solution:
    def numWays(self, steps: int, arrLen: int) -> int:
        """
        arrLen サイズの配列ののインデックス0のポインターを持つ。
        一つのポジションを左か右に1ポジション動かすか、同じ位置止まることができる。
        (ポインターは常に配列の中にいる)

        steps と arrLen の2つの整数が与えられる。
        step を実行した後でもポインターがインデックス 0 にある方法の数を返す。
        答えが大きくなる可能性があるため、10^9+7 を法にして返す。

        i=ステップ数 j=位置に、方法数を入れる DP テーブルを作成する。
        dp[i] のステップ数の位置を1通りで初期化する

        dp[i][j] には、左に移動、止まる、右に移動の3通りが考えられるため、
        dp[i-1][j+1]+dp[i-1][j]+dp[i-1][j-1]を合計したものを設定する。

        メモリー節約のためdpテーブルには、直前のものだけ記録するようにする。

        - Time complexity: O(steps * arrLen)
        - Space complexity: O(arrLen)

        #DP

        Args:
            steps (int): step を実行しする。
            arrLen (int): arrLen サイズの配列を示す。

        Returns:
            int: step を実行した後でもポインターがインデックス 0 にある方法の数を返す。
        """
        mod = 10**9 + 7
        dp: list[list[int]] = [[0] * (arrLen + 1) for _ in range(2)]

        for i in range(steps + 1):
            n = arrLen
            # print(f"i={i}, n={n}")
            if arrLen > i:
                dp[i % 2][i] = 1
                n = i
            # print(f"1: dp={dp}, n={n}")
            for j in range(n - 1, -1, -1):
                dp[i % 2][j] = (
                    dp[(i - 1) % 2][j + 1] + dp[(i - 1) % 2][j] + dp[(i - 1) % 2][j - 1]
                ) % mod

        # print(f"dp={dp}")
        return dp[steps % 2][0]


sol = Solution()
print(sol.numWays(steps=3, arrLen=2))
print(sol.numWays(steps=2, arrLen=4))
print(sol.numWays(steps=4, arrLen=2))
print(sol.numWays(steps=27, arrLen=7))  # 127784505
