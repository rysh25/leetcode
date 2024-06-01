class Solution:
    def scoreOfString(self, s: str) -> int:
        """
        文字列 s が与えられます。文字列のスコアは、隣接する文字の ASCII 値間の絶対差の合計として定義されます。

        スコアを返します。

        - Time complexity: O(n)
        - Space complexity: O(1)

        #String

        Args:
            s (str): 文字列

        Returns:
            int: スコアを返します。
        """
        sum = 0
        for i in range(len(s) - 1):
            sum += abs(ord(s[i + 1]) - ord(s[i]))

        return sum


sol = Solution()
print(sol.scoreOfString(s="hello"))
print(sol.scoreOfString(s="zaz"))
