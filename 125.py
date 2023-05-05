import re


class Solution_tp:
    def isPalindrome(self, s: str) -> bool:
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
        t = s.lower()
        t = re.sub(r"[^0-9a-z]+", "", t)
        return t == t[::-1]


sol = Solution()
print(sol.isPalindrome(s="A man, a plan, a canal: Panama"))
print(sol.isPalindrome(s="race a car"))
print(sol.isPalindrome(s=" "))
print(sol.isPalindrome(s=""))
