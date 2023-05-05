from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = [1] * len(nums)

        prefix = 1
        for i in range(len(nums)):
            ans[i] *= prefix
            prefix *= nums[i]

        suffix = 1
        for i in range(len(nums) - 1, -1, -1):
            ans[i] *= suffix
            suffix *= nums[i]

        return ans


sol = Solution()
print(sol.productExceptSelf(nums=[1, 2, 3, 4]))
print(sol.productExceptSelf([-1, 1, 0, -3, 3]))
