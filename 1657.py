class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        """
        次の操作を使用して一方の文字列をもう一方の文字列から取得できる場合、2 つの文字列は近いと見なされます。

        操作 1: 既存の 2 つのキャラクターを交換します。
        たとえば、abcde -> aecdb
        操作 2: ある既存の文字をすべて別の既存の文字に変換し、他の文字でも同じことを行います。

        2 つの文字列 word1 と word2 を指定すると、word1 と word2 が近い場合は true を返し、そうでない場合は false を返します。


        2つの文字列に出現する文字の種類が同じあった上で、出現数のパターンが一致する場合、操作によって一致させることが可能となる。

        - Time complexity: O(n)
        - Space complexity: O(1)

        Args:
            word1 (str): 文字列
            word2 (str): 文字列

        Returns:
            bool: word1 と word2 が近い場合は true を返し、そうでない場合は false を返します。
        """

        if len(word1) != len(word2):
            return False

        freq1: list[int] = [0] * 26
        freq2: list[int] = [0] * 26

        for i in range(len(word1)):
            freq1[ord(word1[i]) - ord("a")] += 1
            freq2[ord(word2[i]) - ord("a")] += 1

        # 一方に出現する文字が、もう一方にも存在するか
        for i in range(26):
            if not (
                (freq1[i] == 0 and freq2[i] == 0) or (freq1[i] > 0 and freq2[i] > 0)
            ):
                return False

        freq1.sort()
        freq2.sort()

        # 出現数のパターンが一致するか
        for i in range(26):
            if freq1[i] != freq2[i]:
                return False
        return True


sol = Solution()
print(sol.closeStrings(word1="abc", word2="bca"))
print(sol.closeStrings(word1="a", word2="aa"))
print(sol.closeStrings(word1="cabbba", word2="abbccc"))
