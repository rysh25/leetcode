from typing import Set


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        Sliding Window で文字の重複のない最長文字数を数えます。

        文字列を読み進めるための left, right の変数を0で初期化します。
        最長文字数を管理するための変数を用意します。
        文字の出現回数を管理するための集合を用意します。

        right が文字列の最後に行くまで繰り返します。
            right の位置の文字が集合に含まれていル間ループします
                left を進めて、left 位置の文字を集合から消します。
            集合に right 位置の文字を追加します。
            right - left + 1 と最長文字数の大きい方を最長文字数に入れます。

        最長文字数を返します。

        Time complexity: O(N)
        Space complexity: O(N)
        """

        left = 0
        max_length = 0
        occur: Set[str] = set()

        for right in range(len(s)):
            # print(
            #     f"left={left}, s[left]={s[left]}, right={right}, s[right]={s[right]}, occur={occur}"
            # )
            while s[right] in occur:
                occur.remove(s[left])
                left += 1

            occur.add(s[right])
            max_length = max(max_length, right - left + 1)

        return max_length


sol = Solution()
print(sol.lengthOfLongestSubstring(s="abcabcbb"))
print(sol.lengthOfLongestSubstring(s="bbbbb"))
print(sol.lengthOfLongestSubstring(s="pwwkew"))
