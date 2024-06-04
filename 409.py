class Solution:
    def longestPalindrome(self, s: str) -> int:
        """
        小文字または大文字で構成される文字列 s を指定されます。
        これらの文字を使用して構築できる最も長い回文文字列の長さを返します。

        - Time complexity: O(n)
        - Space complexity: O(n)

        #String
        #Greedy

        Args:
            s (str): 文字列

        Returns:
            int: 構築できる最も長い回文文字列の長さを返します。
        """
        from collections import defaultdict

        # print(f"s={s}")

        counts: defaultdict[str, int] = defaultdict(int)

        for c in s:
            counts[c] += 1

        use_odd = False
        ans = 0
        for c in counts:
            if counts[c] % 2 == 1:
                if not use_odd:
                    ans += counts[c]
                    use_odd = True
                else:
                    ans += counts[c] - 1
            else:
                ans += counts[c]

        return ans


sol = Solution()
print(sol.longestPalindrome(s="abccccdd"))
print(sol.longestPalindrome(s="a"))
