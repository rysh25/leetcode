class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        """
        文字列 s を指定すると、2 つの等しい文字の間の 2 つの文字を除いた最長の部分文字列の長さを返します。
        そのような部分文字列がない場合は、-1 を返します。

        - Time complexity: O(n)
        - Space complexity: O(1)

        Args:
            s (str): 文字列

        Returns:
            int:  つの等しい文字の間の 2 つの文字を除いた最長の部分文字列の長さを返します。そのような部分文字列がない場合は、-1 を返します。
        """
        first_index: list[int] = [-1] * 26

        ans = -1
        for i in range(len(s)):
            c = ord(s[i]) - ord("a")

            if first_index[c] == -1:
                first_index[c] = i
            else:
                ans = max(ans, i - first_index[c] - 1)

        return ans


sol = Solution()
print(sol.maxLengthBetweenEqualCharacters(s="aa"))
print(sol.maxLengthBetweenEqualCharacters(s="abca"))
print(sol.maxLengthBetweenEqualCharacters(s="cbzxy"))
