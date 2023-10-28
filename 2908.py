class Solution:
    def minimumSum(self, nums: list[int]) -> int:
        n = len(nums)

        INF = 10**9 + 1
        min_sum: int = INF

        for i in range(n):
            for j in range(i + 1, n):
                for k in range(j + 1, n):
                    if nums[i] < nums[j] and nums[k] < nums[j]:
                        min_sum = min(min_sum, nums[i] + nums[j] + nums[k])

        return min_sum if min_sum != INF else -1


sol = Solution()
# print(sol.minimumSum(nums=[8, 6, 1, 5, 3]))
# print(sol.minimumSum(nums=[5, 4, 8, 7, 10, 2]))
# print(sol.minimumSum(nums=[6, 5, 4, 3, 4, 5]))
print(sol.minimumSum(nums=[49, 50, 48]))  # -1
