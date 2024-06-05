class Solution:
    def commonChars(self, words: list[str]) -> list[str]:
        """
        文字列配列の word を指定すると、その単語内のすべての文字列に出現するすべての文字 (重複を含む) の配列を返します。

        - Time complexity: O(n)
        - Space complexity: O(n)

        Args:
            words (list[str]): 文字列配列

        Returns:
            list[str]: その単語内のすべての文字列に出現するすべての文字 (重複を含む) の配列を返します。
        """
        from collections import defaultdict

        n = len(words)
        counts: list[defaultdict[str, int]] = [defaultdict(int) for _ in range(n)]

        for i in range(n):
            for c in words[i]:
                counts[i][c] += 1

        ans: list[str] = []
        for k in counts[0]:
            ok = True
            mn = counts[0][k]
            for i in range(1, n):
                if 0 == counts[i][k]:
                    ok = False
                    break
                mn = min(mn, counts[i][k])
            if ok:
                for _ in range(mn):
                    ans.append(k)

        return ans


sol = Solution()
print(sol.commonChars(words=["bella", "label", "roller"]))
print(sol.commonChars(words=["cool", "lock", "cook"]))
print(
    sol.commonChars(
        words=[
            "acabcddd",
            "bcbdbcbd",
            "baddbadb",
            "cbdddcac",
            "aacbcccd",
            "ccccddda",
            "cababaab",
            "addcaccd",
        ]
    )
)
