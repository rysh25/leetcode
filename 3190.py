class Solution:
    def minimumOperations(self, nums: list[int]) -> int:

        ans = 0
        for n in nums:
            ans += min(n % 3, 3 - n % 3)

        return ans


sol = Solution()
print(sol.minimumOperations(nums=[1, 2, 3, 4]))
print(sol.minimumOperations(nums=[3, 6, 9]))
