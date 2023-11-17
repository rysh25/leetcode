class Solution:
    def stringCount(self, n: int) -> int:
        MOD = 10**9 + 7
        if n < 4:
            return 0

        ans = 4 * 3

        for _ in range(n - 4):
            ans *= 26

        return ans


sol = Solution()
print(sol.stringCount(n=4))
print(sol.stringCount(n=10))
