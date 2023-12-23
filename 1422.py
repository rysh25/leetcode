class Solution:
    def maxScore(self, s: str) -> int:
        """
        0 と 1 からなるの文字列 s を指定すると、その文字列を空ではない 2 つの部分文字列 (つまり、左の部分文字列と右の部分文字列) に分割した後、最大スコアを返します。

        文字列を分割した後のスコアは、左側の部分文字列のゼロの数と右側の部分文字列の 1 の数を足したものです。

        - Time complexity: O(n)
        - Space complexity: O(1)

        Args:
            s (str): 0 と 1 からなるの文字列

        Returns:
            int: 最大スコアを返します。
        """
        ans = 0
        for i in range(1, len(s)):
            # print(f"0: {s[:i]}, 1: {s[i:]}")
            ans = max(ans, s[:i].count("0") + s[i:].count("1"))

        return ans


sol = Solution()
print(sol.maxScore(s="011101"))
print(sol.maxScore(s="00111"))
print(sol.maxScore(s="1111"))
print(sol.maxScore(s="00"))  # 1
print(sol.maxScore(s="01001"))  # 4
