class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """
        s と t がアナグラムか調べるため、お互いにソートし、違いがあるかを調べる

        Time complexity: O(n long n)
        Space complexity: O(n)
        """
        return sorted(s) == sorted(t)
