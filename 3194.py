class Solution:
    def minimumAverage(self, nums: list[int]) -> float:
        n = len(nums)
        nums.sort()

        ans = 1001001001
        for i in range(n // 2):
            ans = min(ans, (nums[i] + nums[n - i - 1]) / 2)

        return ans


sol = Solution()
print(sol.minimumAverage(nums=[7, 8, 3, 4, 15, 13, 4, 1]))
print(sol.minimumAverage(nums=[1, 9, 8, 3, 10, 5]))
print(sol.minimumAverage(nums=[1, 2, 3, 7, 8, 9]))
