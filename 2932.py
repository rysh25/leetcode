class Solution:
    def maximumStrongPairXor(self, nums: list[int]) -> int:
        ans = 0
        for i in range(len(nums) - 1):
            x = nums[i]
            for j in range(i + 1, len(nums)):
                y = nums[j]
                if abs(x - y) > min(x, y):
                    continue

                if ans < x ^ y:
                    ans = x ^ y
        return ans


sol = Solution()
print(sol.maximumStrongPairXor(nums=[1, 2, 3, 4, 5]))
print(sol.maximumStrongPairXor(nums=[10, 100]))
print(sol.maximumStrongPairXor(nums=[5, 6, 25, 30]))
