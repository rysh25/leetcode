class Solution:
    def distributeCandies(self, n: int, limit: int) -> int:
        count = 0

        for i in range(min(n, limit) + 1):
            for j in range(min(n - i, limit) + 1):
                if n - i - j <= limit:
                    count += 1
        return count


sol = Solution()
print(sol.distributeCandies(n=5, limit=2))
print(sol.distributeCandies(n=3, limit=3))
