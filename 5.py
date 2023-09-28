class Solution:
    def longestPalindrome(self, s: str) -> str:
        """
        文字列 s が与えられる。
        最も長い回文を返す。

        全パターンを回文かチェックすると回文のチェックが O(n) のため、
        O(n^3)かかり制限に間に合わなくなる。

        中心を0からずらしながら左右に回文かチェックするようにすと O(n^2) となり、
        制限に間に合う。

        - Time complexity: O(n^2)
        - Space complexity: O(n)

        Args:
            s (str): 文字列 s が与えられる。

        Returns:
            str: 最も長い回文を返す。
        """
        max_len = 0
        ans = ""
        for i in range(len(s)):
            # print(f"i={i}")
            len_wk, t = self.palindrome(s, i, i)  # Odd
            # print(f"Odd: len_wk={len_wk}, t={t}")
            if max_len < len_wk:
                max_len = len_wk
                ans = t
            len_wk, t = self.palindrome(s, i, i + 1)  # Even
            # print(f"Even: len_wk={len_wk}, t={t}")
            if max_len < len_wk:
                max_len = len_wk
                ans = t

        return ans

    def palindrome(self, s: str, l: int, r: int) -> tuple[int, str]:
        found = False
        while 0 <= l and r < len(s) and s[l] == s[r]:
            found = True
            l -= 1
            r += 1
        if found:
            return (r - l + 1, s[l + 1 : r])
        else:
            return 0, ""


sol = Solution()
print(sol.longestPalindrome(s="babad"))
print(sol.longestPalindrome(s="cbbd"))
print(sol.longestPalindrome(s="a"))
