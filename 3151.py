class Solution:
    def isArraySpecial(self, nums: list[int]) -> bool:
        ans = True

        for i in range(len(nums) - 1):
            if nums[i] % 2 == nums[i + 1] % 2:
                ans = False

        return ans


sol = Solution()
print(sol.isArraySpecial(nums=[1]))
print(sol.isArraySpecial(nums=[2, 1, 4]))
print(sol.isArraySpecial(nums=[4, 3, 1, 6]))
