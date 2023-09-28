class Solution:
    def rob(self, nums: list[int]) -> int:
        """
        通り沿いの家に泥棒に入る。
        各家に隠してあるお金は、nums 配列で渡される。
        隣接する家に盗みに入ると自動的に警察に連絡される。
        警察に連絡されることなく、盗むことができる最大の金額を返す。

        - Time complexity: O(n)
        - Space complexity: O(n)

        #DP

        Args:
            nums (list[int]): 各家に隠してあるお金が渡される。

        Returns:
            int: 盗むことができる最大の金額を返す。
        """
        dp: list[int] = [0] * (len(nums) + 1)

        for i in range(1, len(nums) + 1):
            dp[i] = max(dp[i - 2] + nums[i - 1], dp[i - 1])

        return dp[-1]


sol = Solution()
print(sol.rob(nums=[1, 2, 3, 1]))
print(sol.rob(nums=[2, 7, 9, 3, 1]))
