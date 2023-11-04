class Solution:
    def sumCounts(self, nums: list[int]) -> int:
        n = len(nums)
        ans = 0
        for i in range(n):
            for j in range(i, n):
                s: set[int] = set()
                # print(f"i={i}, j={j}")
                for k in range(i, j + 1):
                    # print(f"k={k}")
                    s.add(nums[k])
                # print(f"len(s)={len(s)}")
                ans += len(s) * len(s)

        return ans


sol = Solution()
print(sol.sumCounts(nums=[1, 2, 1]))
print(sol.sumCounts(nums=[1, 1]))
