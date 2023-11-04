class Solution:
    def minChanges(self, s: str) -> int:
        count = 0
        for i in range(0, len(s), 2):
            if s[i] != s[i + 1]:
                count += 1

        return count


sol = Solution()
print(sol.minChanges(s="1001"))
print(sol.minChanges(s="10"))
print(sol.minChanges(s="0000"))
print(sol.minChanges(s="0001"))
