class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        """
        英語の小文字のみで構成される 2 つの文字列 s と t が与えられます。

        t が s の部分列になるように s の末尾に追加する必要がある文字の最小数を返します。

        #String
        #TwoPointers
        #Greedy

        - Time complexity: O(n)
        - Space complexity: O(1)

        Args:
            s (str): 英語の小文字のみで構成される文字列
            t (str): 英語の小文字のみで構成される文字列

        Returns:
            int: t が s の部分列になるように s の末尾に追加する必要がある文字の最小数を返します。
        """

        si, ti = 0, 0

        while si < len(s) and ti < len(t):
            if s[si] == t[ti]:
                ti += 1

            si += 1

        # print(f"si={si}, ti={ti}")

        return len(t) - ti


sol = Solution()
print(sol.appendCharacters(s="coaching", t="coding"))
print(sol.appendCharacters(s="abcde", t="a"))
print(sol.appendCharacters(s="z", t="abcde"))
