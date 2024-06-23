class Solution:
    def minOperations(self, nums: list[int]) -> int:
        count = 0
        if nums[0] == 0:
            count = 1
        prev = nums[0]

        for i in range(1, len(nums)):
            if prev != nums[i]:
                count += 1

            prev = nums[i]

        return count


sol = Solution()
print(sol.minOperations(nums=[0, 1, 1, 0, 1]))
print(sol.minOperations(nums=[1, 0, 0, 0]))
print(sol.minOperations(nums=[0, 1, 1, 0, 1]))  # 4
