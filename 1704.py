class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        """
        偶数の長さの文字列 s が与えられます。 この文字列を同じ長さの 2 つの半分に分割し、前半を a、後半を b とします。

        2 つの文字列は、同じ数の母音 ('a'、'e'、'i'、'o'、'u'、'A'、'E'、'I'、'O'、') を持っていれば似ています。 う」）。 s には大文字と小文字が含まれることに注意してください。

        a と b が似ている場合は true を返します。 それ以外の場合は false を返します。

        - Time complexity: O(n)
        - Space complexity: O(1)

        Args:
            s (str): 偶数の長さの文字列

        Returns:
            bool: a と b が似ている場合は true を返します。
        """

        def count_volwels(s: str):
            count = 0
            for c in s:
                if c.lower() in ["a", "e", "i", "o", "u"]:
                    count += 1
            return count

        return count_volwels(s[: len(s) // 2]) == count_volwels(s[len(s) // 2 :])


sol = Solution()
print(sol.halvesAreAlike(s="book"))
print(sol.halvesAreAlike(s="textbook"))
print(sol.halvesAreAlike(s="tkPAdxpMfJiltOerItiv"))
