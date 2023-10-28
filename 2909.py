class Solution:
    def minimumSum(self, nums: list[int]) -> int:
        n = len(nums)

        INF = 10**9 + 1
        min_left = [INF] * n
        min_right = [INF] * n

        for i in range(1, n):
            min_left[i] = min(min_left[i - 1], nums[i - 1])

        for i in range(n - 2, -1, -1):
            min_right[i] = min(min_right[i + 1], nums[i + 1])

        min_sum = INF
        for j in range(1, n - 1):
            if nums[j] > min_left[j] and nums[j] > min_right[j]:
                min_sum = min(min_sum, nums[j] + min_left[j] + min_right[j])

        return min_sum if min_sum != INF else -1


sol = Solution()
print(sol.minimumSum(nums=[8, 6, 1, 5, 3]))
print(sol.minimumSum(nums=[5, 4, 8, 7, 10, 2]))
print(sol.minimumSum(nums=[6, 5, 4, 3, 4, 5]))
print(sol.minimumSum(nums=[49, 50, 48]))  # -1
print(sol.minimumSum(nums=[8, 6, 1, 5, 3]))  # 9
