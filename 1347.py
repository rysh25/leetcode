class Solution:
    def minSteps(self, s: str, t: str) -> int:
        """
        同じ長さの 2 つの文字列 s と t が与えられます。 1 つのステップで、t の任意の文字を選択し、別の文字に置き換えることができます。

        t を s のアナグラムにするための最小ステップ数を返します。

        Args:
            s (str): 文字列
            t (str): 文字列

        Returns:
            int: t を s のアナグラムにするための最小ステップ数を返します。
        """
        from collections import defaultdict

        freq: defaultdict[str, int] = defaultdict(int)

        for c in s:
            freq[c] += 1

        for c in t:
            freq[c] -= 1

        ans = 0
        for k in freq:
            ans += abs(freq[k])

        return (ans + 1) // 2


sol = Solution()
print(sol.minSteps(s="bab", t="aba"))
print(sol.minSteps(s="leetcode", t="practice"))
print(sol.minSteps(s="anagram", t="mangaar"))
