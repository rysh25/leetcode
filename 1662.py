class Solution:
    def arrayStringsAreEqual(self, word1: list[str], word2: list[str]) -> bool:
        """
        2 つの文字列配列 word1 と word2 を指定すると、
        2 つの配列が同じ文字列を表す場合は true を返し、それ以外の場合は false を返します。

        - Time complexity: O(n)
        - Space complexity: O(1)

        Args:
            word1 (list[str]): 文字列配列
            word2 (list[str]): 文字列配列

        Returns:
            bool: 2 つの配列が同じ文字列を表す場合は true を返し、それ以外の場合は false を返します。
        """
        return "".join(word1) == "".join(word2)


sol = Solution()
print(sol.arrayStringsAreEqual(word1=["ab", "c"], word2=["a", "bc"]))
print(sol.arrayStringsAreEqual(word1=["a", "cb"], word2=["ab", "c"]))
print(sol.arrayStringsAreEqual(word1=["abc", "d", "defg"], word2=["abcddefg"]))
