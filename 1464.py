class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        """
        整数の配列 nums が与えられます。
        その配列の 2 つの異なるインデックス i と j を選択します。
        (nums[i]-1)*(nums[j]-1) の最大値を返します。

        - Time complexity: O(n log n)
        - Space complexity: O(1)

        Args:
            nums (list[int]): 整数の配列

        Returns:
            int: (nums[i]-1)*(nums[j]-1) の最大値を返します。
        """
        nums.sort()
        return (nums[-1] - 1) * (nums[-2] - 1)


sol = Solution()
print(sol.maxProduct(nums=[3, 4, 5, 2]))
print(sol.maxProduct(nums=[1, 5, 4, 5]))
print(sol.maxProduct(nums=[3, 7]))
