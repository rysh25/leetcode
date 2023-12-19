class Solution:
    def maxProductDifference(self, nums: list[int]) -> int:
        """
        2 つのペア (a, b) と (c, d) の積の差は、(a * b) - (c * d) として定義されます。

        整数配列 nums が渡されます。
        ペア (nums[w], nums[x]) と (nums[y], nums[z]) の積の差が最大になるように 4 つの異なるインデックス w、x、y、z を選択します。 。

        そのような積の差の最大値を返します。

        - Time complexity: O(n log n)
        - Space complexity: O(1)

        Args:
            nums (list[int]): 整数配列

        Returns:
            int: 積の差の最大値を返します。
        """
        nums.sort()
        return (nums[-1] * nums[-2]) - (nums[1] * nums[0])


sol = Solution()
print(sol.maxProductDifference(nums=[5, 6, 2, 7, 4]))
print(sol.maxProductDifference(nums=[4, 2, 5, 9, 7, 4, 8]))
