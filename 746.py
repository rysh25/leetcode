class Solution:
    def minCostClimbingStairs(self, cost: list[int]) -> int:
        """
        整数配列 cost が与えられる。ここで cost[i] は、階段のi番目のステップのコストである。
        一度コストを払うと、1段でも2段登ることができる。
        0段目からも2段目からも開始することができる。
        フロアの最上部に到達するための最小のコストはを返す。

        - Time complexity: O(n)
        - Space complexity: O(n)

        #DP

        Args:
            cost (list[int]): 整数配列 cost が与えられる。

        Returns:
            int: フロアの最上部に到達するための最小のコストはを返す。
        """
        dp: list[int] = [0] * (len(cost) + 1)

        for i in range(2, len(cost) + 1):
            dp[i] = min(dp[i - 2] + cost[i - 2], dp[i - 1] + cost[i - 1])

        return dp[len(cost)]


sol = Solution()
print(sol.minCostClimbingStairs(cost=[10, 15, 20]))
print(sol.minCostClimbingStairs(cost=[1, 100, 1, 1, 1, 100, 1, 1, 100, 1]))
