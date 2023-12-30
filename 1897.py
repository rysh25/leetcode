class Solution:
    def makeEqual(self, words: list[str]) -> bool:
        from collections import defaultdict

        """
        文字列単語の配列 (0 からインデックス付き) が与えられます。

        1 回の操作で、2 つの異なるインデックス i と j (words[i] は空ではない文字列) を選択し、
        words[i] の任意の文字を words[j] 内の任意の位置に移動します。

        任意の数の操作を使用してワード内のすべての文字列を等しくできる場合は true を返し、
        そうでない場合は false を返します。


        各文字の出現頻度が words 配列の長さで割り切れるならすべての文字列を等しくすることができる。

        Args:
            words (list[str]): 文字列単語の配列

        Returns:
            bool: 任意の数の操作を使用してワード内のすべての文字列を等しくできる場合は true を返し、そうでない場合は false を返します。

        """
        freq: defaultdict[str, int] = defaultdict(int)
        for i in range(len(words)):
            for c in words[i]:
                freq[c] += 1

        for k in freq:
            if freq[k] % len(words) != 0:
                return False

        return True


sol = Solution()
print(sol.makeEqual(words=["abc", "aabc", "bc"]))
print(sol.makeEqual(words=["ab", "a"]))
