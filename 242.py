class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """
        2つの文字列 s と t が与えられる。t が s のアナグラムなら true、
        そうでないなら false を返す。

        s と t がアナグラムか調べるため、お互いにソートし、違いがあるかを調べる

        Time complexity: O(n long n)
        Space complexity: O(n)

        #Array
        """
        return sorted(s) == sorted(t)
