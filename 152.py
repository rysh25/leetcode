class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        """
        整数の配列 nums が渡される。
        最も大きい連続部分配列の積を見つけて返す。

        DP テーブルに、nums[i] を利用する場合の最大値と最小値を記録する。
        マイナス同士をかけると大きくなる可能性があるので、最大と最小を記録する。

        Kadane's Algorithm

        - Time complexity: O(n)
        - Space complexity: O(n)

        #DP
        #Kadane

        Args:
            nums (list[int]): 整数の配列 nums が渡される。

        Returns:
            int: 最も大きい連続部分配列の積を見つけて返す。
        """
        dp_min: list[int] = [0] * len(nums)
        dp_max: list[int] = [0] * len(nums)
        dp_min[0] = nums[0]
        dp_max[0] = nums[0]
        for i in range(1, len(nums)):
            dp_min[i] = min(nums[i], dp_min[i - 1] * nums[i], dp_max[i - 1] * nums[i])
            dp_max[i] = max(nums[i], dp_min[i - 1] * nums[i], dp_max[i - 1] * nums[i])

        # print(f"dp_min={dp_min}")
        # print(f"dp_max={dp_max}")

        return max(dp_max)


sol = Solution()
print(sol.maxProduct(nums=[2, 3, -2, 4]))
print(sol.maxProduct(nums=[-2, 0, -1]))
print(sol.maxProduct(nums=[-2, 3, -4]))  # 24
