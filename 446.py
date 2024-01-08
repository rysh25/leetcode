from collections import defaultdict


class Solution:
    def numberOfArithmeticSlices(self, nums: list[int]) -> int:
        """
        与えられた整数配列 nums に対して、nums のすべての等差数列の数を返します。

        数列は、少なくとも三つの要素で構成され、連続する任意の二つの要素の差が同じ場合に等差数列と呼ばれます。


        n * n の dp 配列を用意する
        dp[i][j] には、i を終端とする差が j の等差数列の数が入る。
        total として、等差数列が3を超えるの数列の数を数える。
        これが答えとなる。

        - Time complexity: O(n * n)
        - Space complexity: O(n * n)

        #DP

        Args:
            nums (list[int]): 整数配列

        Returns:
            int: nums のすべての等差数列の数を返します。
        """
        n = len(nums)
        total_count = 0
        dp: list[defaultdict[int, int]] = [defaultdict(int) for _ in range(n)]

        for i in range(1, n):
            for j in range(i):
                diff = nums[i] - nums[j]
                dp[i][diff] += 1
                if diff in dp[j]:
                    dp[i][diff] += dp[j][diff]
                    total_count += dp[j][diff]
        print(f"dp={dp}")

        return total_count


sol = Solution()
print(sol.numberOfArithmeticSlices(nums=[2, 4, 6, 8, 10]))
print(sol.numberOfArithmeticSlices(nums=[7, 7, 7, 7, 7]))
