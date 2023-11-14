class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        """
        文字列 s を指定すると、s の部分列である長さ 3 の一意の回文の数を返します。

        - Time complexity: O(n)
        - Space complexity: O(n)

        Args:
            s (str): 文字列

        Returns:
            int: s の部分列である長さ 3 の一意の回文の数を返します。
        """
        INF = 10**9 + 1
        first_index: list[int] = [INF] * 26
        last_index: list[int] = [INF] * 26

        for i, c in enumerate(s):
            first_index[ord(c) - ord("a")] = min(first_index[ord(c) - ord("a")], i)
            last_index[ord(c) - ord("a")] = i

        ans = 0
        for i in range(26):
            c = chr(ord("a") + i)
            first, last = first_index[ord(c) - ord("a")], last_index[ord(c) - ord("a")]
            if first == INF:
                continue
            ans += len(set(s[first + 1 : last]))

        return ans


sol = Solution()
print(sol.countPalindromicSubsequence(s="aabca"))
print(sol.countPalindromicSubsequence(s="adc"))
print(sol.countPalindromicSubsequence(s="bbcbaba"))
