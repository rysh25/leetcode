class Solution:
    def countSubstrings(self, s: str) -> int:
        """
        文字列 s が与えられる
        その中の回文文字列の数を返す。

        全パターン O(n^2) を回文かチェックすると回文のチェックが O(n) のため、
        O(n^3)かかり制限に間に合わなくなる。

        中心を0からずらしながら左右に回文かチェックするようにすと O(n^2) となり、
        制限に間に合う。

        Args:
            s (str): 文字列 s が与えられる

        - Time complexity: O(n^2)
        - Space complexity: O(1)

        Returns:
            int: 回文文字列の数を返す。
        """
        ans = 0

        for i in range(len(s)):
            ans += self.count_palindrome(s, i, i)  # odd
            if i > 0:
                ans += self.count_palindrome(s, i - 1, i)  # even
        return ans

    def count_palindrome(self, s: str, l: int, r: int) -> int:
        count = 0
        # print(f"count_palindrome: l={l}, r={r}, {s[l:r+1]}")
        while 0 <= l and r < len(s):
            if s[l] == s[r]:
                count += 1
            else:
                break
            l -= 1
            r += 1
        # print(f"count={count}")
        return count


sol = Solution()
print(sol.countSubstrings(s="abc"))
print(sol.countSubstrings(s="aaa"))
