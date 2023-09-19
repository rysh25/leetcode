class Solution:
    def subsetsWithDup(self, nums: list[int]) -> list[list[int]]:
        """
        重複を含むの整数配列が指定されます。
        すべての部分集合 (Subset) を返します。

        バックトラックで再帰的に部分集合を作成します。

        - Time complexity: O(2^n)
        - Space complexity: O(n)

        #BackTracking

        Args:
            nums (list[int]): 重複を含むの整数配列を指定します。

        Returns:
            list[list[int]]: すべての部分集合を返します。
        """

        ans: list[list[int]] = []

        nums.sort()

        def backtrack(i: int, curr: list[int]):
            if i >= len(nums):
                ans.append(curr[:])
                return

            curr.append(nums[i])
            backtrack(i + 1, curr)

            curr.pop()

            while i + 1 < len(nums) and nums[i] == nums[i + 1]:
                i += 1
            backtrack(i + 1, curr)

        backtrack(0, [])
        return ans


sol = Solution()
print(sol.subsetsWithDup(nums=[1, 2, 2]))
print(sol.subsetsWithDup(nums=[0]))
