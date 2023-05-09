import re


class Solution_tp:
    def isPalindrome(self, s: str) -> bool:
        """
        尺取り法 (Two Pointers) で、与えられた文字列が回文であるか調べる。

        左と、右から同時に順番に文字を比べていく。
        その際、英数字以外は読み飛ばす。
        ぶつかるまで全て同じ文字であれば回文と判断する。

        Time complexity: O(n)
        Space complexity: O(1)

        #TwoPointers
        """

        left = 0
        right = len(s) - 1
        while left < right:
            # print(f"left={left}, right={right}")
            if not s[left].isalnum():
                left += 1
                continue
            if not s[right].isalnum():
                right -= 1
                continue

            if s[left].lower() == s[right].lower():
                left += 1
                right -= 1
            else:
                return False

        return True


class Solution:
    def isPalindrome(self, s: str) -> bool:
        """
        英数字以外を削除し、与えられた文字列と、反転した文字列を比較し
        同じであれば回文と判断する。

        Time complexity: O(N)
        Space complexity: O(1)
        """
        t = s.lower()
        t = re.sub(r"[^0-9a-z]+", "", t)
        return t == t[::-1]


sol = Solution()
print(sol.isPalindrome(s="A man, a plan, a canal: Panama"))
print(sol.isPalindrome(s="race a car"))
print(sol.isPalindrome(s=" "))
print(sol.isPalindrome(s=""))
