class Solution:
    def getSumAbsoluteDifferences(self, nums: list[int]) -> list[int]:
        """
        非降順でソートされた整数配列 nums が与えられます。

        result[i] が nums[i] と配列内の他のすべての要素との差の絶対値の合計と等しくなるように、nums と同じ長さの整数配列の結果を作成して返します。


        result のすべて要素をナイーブに求めると O(n^2) かかるため間に合わない。
        nums がソートされているため、result[i] は、nums[i] * i - それより前の合計 + nums[i] * (n-i-1) - それより後ろの合計となる。
        prefix_sum を作成することで、O(n) で求めることができる。

        - Time complexity: O(n)
        - Space complexity: O(n)

        #PrefixSum

        Args:
            nums (list[int]): 非降順でソートされた整数配列

        Returns:
            list[int]: result[i] が nums[i] と配列内の他のすべての要素との差の絶対値の合計と等しくなるように、nums と同じ長さの整数配列の結果を作成して返します。
        """
        n = len(nums)
        prefix_sum: list[int] = [0] * (n + 1)
        for i in range(n):
            prefix_sum[i + 1] = prefix_sum[i] + nums[i]

        # print(f"prefix_sum={prefix_sum}")

        ans: list[int] = [0] * n
        for i in range(n):
            ans[i] += nums[i] * i - prefix_sum[i]
            # print(f"ans={ans[i]}")
            ans[i] += prefix_sum[n] - prefix_sum[i + 1] - nums[i] * (n - i - 1)
            # print(f"ans={ans[i]}")

        return ans


sol = Solution()
print(sol.getSumAbsoluteDifferences(nums=[2, 3, 5]))
print(sol.getSumAbsoluteDifferences(nums=[1, 4, 6, 8, 10]))
