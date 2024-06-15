class Solution:
    def minIncrementForUnique(self, nums: list[int]) -> int:
        """
        整数配列 nums が与えられます。
        1 回の操作で、0 = i nums.length となるインデックス i を選択し、nums[i] を 1 ずつ増分できます。

        nums のすべての値を一意にするための最小操作数を返します。

        - Time complexity: O(n)
        - Space complexity: O(1)

        Args:
            nums (list[int]): 整数配列

        Returns:
            int: すべての値を一意にするための最小操作数を返します。
        """

        n = len(nums)
        nums.sort()
        ans = 0
        prev = -1
        # print(f"nums={nums}")
        for i in range(n):
            curr = nums[i]
            if prev >= curr:
                curr = prev + 1
                ans += curr - nums[i]

            prev = curr

        return ans


sol = Solution()
print(sol.minIncrementForUnique(nums=[1, 2, 2]))
print(sol.minIncrementForUnique(nums=[3, 2, 1, 2, 1, 7]))
print(sol.minIncrementForUnique(nums=[1, 1]))
print(sol.minIncrementForUnique(nums=[0, 2, 2]))  # 1
print(sol.minIncrementForUnique(nums=[7, 2, 7, 2, 1, 4, 3, 1, 4, 8]))  # 16
