class Solution:
    def valueAfterKSeconds(self, n: int, k: int) -> int:
        MOD = 10**9 + 7

        ans = [1] * n

        for _ in range(k):
            for i in range(1, n):
                ans[i] = (ans[i] + ans[i - 1]) % MOD

        return ans[-1] % MOD


sol = Solution()
# print(sol.valueAfterKSeconds(n=4, k=5))
# print(sol.valueAfterKSeconds(n=4, k=5))
print(sol.valueAfterKSeconds(n=5, k=100))
print(sol.valueAfterKSeconds(n=5, k=1))
