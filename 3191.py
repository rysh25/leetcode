class Solution:
    def minOperations(self, nums: list[int]) -> int:
        ans = 0
        for i in range(len(nums)):
            print(f"i={i}")
            if nums[i] == 0 and i <= len(nums) - 3:
                for j in range(i, i + 3):
                    nums[j] ^= 0 ^ 1

                ans += 1
                # print(f"nums={nums}")

        # print(f"nums={nums}")

        if sum(nums) == len(nums):
            return ans

        return -1


sol = Solution()
print(sol.minOperations(nums=[0, 1, 1, 1, 0, 0]))
print(sol.minOperations(nums=[0, 1, 1, 1]))
