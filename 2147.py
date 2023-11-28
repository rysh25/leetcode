class Solution:
    def numberOfWays(self, corridor: str) -> int:
        """
        廊下を椅子が2つになるように最大1つの仕切りで仕切る。

        Args:
            corridor (str): 文字「S」と「P」で構成される、長さ n の 0 から始まる文字列

        Returns:
            int: コリドーを分割する方法の数を返します。 答えは非常に大きい可能性があるため、10^9 + 7 を法にして返します。
        """
        MOD = 10**9 + 7

        seats = 0
        ans = 1
        l, r = -1, -1
        for i in range(len(corridor)):
            if corridor[i] != "S":
                continue

            seats += 1

            if seats > 0 and seats % 2 == 0:
                l = i
            elif seats > 1 and seats % 2 == 1:
                r = i
                # print(f"i={i}, l={l}, r={r}")
                ans = ans * (r - l) % MOD

        if seats == 0 or seats % 2 == 1:
            return 0
        elif seats == 2:
            return 1

        return ans


sol = Solution()
print(sol.numberOfWays(corridor="SSPPSPS"))
print(sol.numberOfWays(corridor="PPSPSP"))
print(sol.numberOfWays(corridor="S"))
print(sol.numberOfWays(corridor="SPPSSSSPPS"))  # 1
