class Solution:
    def returnToBoundaryCount(self, nums: list[int]) -> int:
        n = len(nums)

        ans = 0
        curr = 0
        for i in range(n):
            curr += nums[i]

            if curr == 0:
                ans += 1

        return ans


sol = Solution()
print(sol.returnToBoundaryCount(nums=[2, 3, -5]))
print(sol.returnToBoundaryCount(nums=[3, 2, -3, -4]))
