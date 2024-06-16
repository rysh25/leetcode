class Solution:
    def numberOfChild(self, n: int, k: int) -> int:
        right = True
        while k >= n - 1:
            k -= n - 1
            right = not right
            print(f"k={k}, right={right}")

        if not right:
            k = n - 1 - k
        return k


sol = Solution()
print(sol.numberOfChild(n=3, k=5))
print(sol.numberOfChild(n=5, k=6))
print(sol.numberOfChild(n=4, k=2))
print(sol.numberOfChild(n=5, k=8))
