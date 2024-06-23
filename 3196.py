class Solution:
    def maximumTotalCost(self, nums: list[int]) -> int:
        """
        長さ n の整数配列 nums が与えられます。

        部分配列 nums[l..r] (0 = l = r n) の cost は次のように定義されます。

        cost (l, r) = nums[l] - nums[l + 1] + ... + nums[r] * (−1)^(r−l)

        あなたのタスクは、部分配列の総 cost が最大になるように nums を部分配列に分割し、各要素が 1 つの部分配列に確実に属するようにすることです。

        配列を最適に分割した後の部分配列の最大合計コストを示す整数を返します。

        注: nums が部分配列に分割されていない場合、つまり k = 1 の場合、総コストは単純にコスト(0, n - 1) になります。


        部分配列はいつでも始めることができる。
        ただし、部分配列の開始時点では反転を選択することはできない。
        また、反転を連続することもできない。
        nums[i] をそのまま使った時の最大値を dp[i][0]に、反転した時の最大値を dp[i][1] に記録する。
        nums[i] をそのまま使うか、反転するかは、1つ前時点でのそれぞれの合計によって決めることができる。

        #DP

        - Time complexity: O(n)
        - Space complexity: O(1)

        Args:
            nums (list[int]): 長さ n の整数配列

        Returns:
            int: 配列を最適に分割した後の部分配列の最大合計コストを示す整数を返します。
        """
        n = len(nums)

        dp: list[list[int]] = [[0] * 2 for _ in range(n)]

        dp[0][0] = nums[0]
        dp[0][1] = -1001001001

        for i in range(1, n):
            dp[i][0] = max(dp[i - 1][0], dp[i - 1][1]) + nums[i]
            dp[i][1] = dp[i - 1][0] - nums[i]

        # print(f"dp={dp}")

        return max(dp[n - 1][0], dp[n - 1][1])


sol = Solution()
print(sol.maximumTotalCost(nums=[1, -2, 3, 4]))
print(sol.maximumTotalCost(nums=[1, -1, 1, -1]))
print(sol.maximumTotalCost(nums=[0]))
print(sol.maximumTotalCost(nums=[1, -1]))
print(sol.maximumTotalCost(nums=[-11, 12, 6]))  # 7
print(sol.maximumTotalCost(nums=[-14, -13, -20]))  # -7
