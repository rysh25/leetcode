class Solution:
    def hasTrailingZeros(self, nums: list[int]) -> bool:
        even_count = 0
        for i in nums:
            if i % 2 == 0:
                even_count += 1

        return True if even_count > 1 else False


sol = Solution()
print(sol.hasTrailingZeros(nums=[1, 2, 3, 4, 5]))
print(sol.hasTrailingZeros(nums=[2, 4, 8, 16]))
print(sol.hasTrailingZeros(nums=[1, 3, 5, 7, 9]))
