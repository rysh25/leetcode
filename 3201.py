class Solution:
    def maximumLength(self, nums: list[int]) -> int:
        n = len(nums)
        parities: list[int] = [0] * n

        for i in range(n):
            parities[i] = nums[i] % 2

        ans = 0

        count = 0

        for i in range(n):
            count += 1 if parities[i] == 0 else 0
        ans = max(ans, count)
        count = 0
        for i in range(n):
            count += 1 if parities[i] == 1 else 0
        ans = max(ans, count)
        count = 0
        j = 0
        for i in range(n):
            if j % 2 == parities[i]:
                count += 1
                j += 1
        ans = max(ans, count)
        count = 0
        j = 1
        for i in range(n):
            if j % 2 == parities[i]:
                count += 1
                j += 1
        ans = max(ans, count)
        count = 0

        return ans


sol = Solution()
print(sol.maximumLength(nums=[1, 2, 3, 4]))
print(sol.maximumLength(nums=[1, 2, 1, 1, 2, 1, 2]))
print(sol.maximumLength(nums=[1, 3]))
