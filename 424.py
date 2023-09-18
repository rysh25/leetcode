from collections import defaultdict


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        """文字列 s と、整数 k が与えられる。
        任意の文字を選択し、任意の英大文字に置き換える操作を最大 k 回行うことができる。

        この操作を行った後同じ文字を含む最長の部分文字列を返します。

        尺取り法(Sliding Window) で、左右のポインターに挟まれた範囲の文字列をについて、繰り返し調べる。
        最長の文字列は、出現した文字の最も多い頻度数+k か文字数の小さい方となる。

        - Time complexity: O(26n) ≈ O(n)
        - Space complexity: O(26) ≈ O(1)

        #SlidingWindow

        Args:
            s (str): 文字列が指定されます。
            k (int): 操作の最大試行回数が指定されます。

        Returns:
            int: 操作を行った後同じ文字を含む最長の部分文字列を返します。
        """

        l = 0
        freq: defaultdict[str, int] = defaultdict(int)
        max_freq = 0
        for r, c in enumerate(s):
            freq[c] += 1
            cur_max_freq = max(freq.values())
            print(f"r={r}, c={c}, cur_max_freq={cur_max_freq}")
            max_freq = max(cur_max_freq, max_freq)
            if cur_max_freq + k < r - l + 1:
                freq[s[l]] -= 1
                l += 1

        return min(max_freq + k, len(s))


sol = Solution()
print(sol.characterReplacement(s="ABA", k=2))
print(sol.characterReplacement(s="ABAB", k=2))
print(sol.characterReplacement(s="AABABBA", k=1))
