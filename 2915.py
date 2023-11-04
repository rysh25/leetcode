class Solution:
    def lengthOfLongestSubsequence(self, nums: list[int], target: int) -> int:
        n = len(nums)
        INF = 10**9 + 1
        dp: list[list[int]] = [[-INF] * (target + 1) for _ in range(n + 1)]
        dp[0][0] = 0
        for i in range(1, n + 1):
            for j in range(target + 1):
                # print(f"i={i}, j={j}, nums[i-1]={nums[i-1]}")
                if j - nums[i - 1] < 0:
                    dp[i][j] = dp[i - 1][j]
                else:
                    # print(
                    #     f"!!!dp[i - 1][j - nums[i - 1]+1={dp[i - 1][j - nums[i - 1]]+1}"
                    # )
                    # print(f"!!!max={}")
                    dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - nums[i - 1]] + 1)
        # print(f"dp={dp}")
        return -1 if dp[n][target] < 0 else dp[n][target]


sol = Solution()
print(sol.lengthOfLongestSubsequence(nums=[1, 2, 3, 4, 5], target=9))
print(sol.lengthOfLongestSubsequence(nums=[4, 1, 3, 2, 1, 5], target=7))
print(sol.lengthOfLongestSubsequence(nums=[1, 1, 5, 4, 5], target=3))
