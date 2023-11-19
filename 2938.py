class Solution:
    def minimumSteps(self, s: str) -> int:
        ans = 0
        white_left = 0
        for i in range(len(s)):
            if s[i] == "0":
                ans += i - white_left
                white_left += 1
        return ans


sol = Solution()
print(sol.minimumSteps(s="101"))
print(sol.minimumSteps(s="100"))
print(sol.minimumSteps(s="0111"))
