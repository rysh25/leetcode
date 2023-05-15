class Solution_bk:
    def permute(self, nums: list[int]) -> list[list[int]]:
        """
        個別の整数からなるの整数配列が指定されます。
        すべての順列を返します。

        バックトラッキングで再帰的に順列のリストを作成します。

        Time complexity: O(n!)
        Space complexity: O(n*n!)

        n は nums リストの長さです。

        #BackTracking

        Args:
            nums (list[int]): 個別の整数からなるの整数配列を指定します。

        Returns:
            list[list[int]]: 指定された整数配列の順列のリストを返します。
        """
        ans: list[list[int]] = []

        def backtrack(i: int, nums: list[int], curr: list[int] = []):
            if not nums:
                ans.append(curr.copy())
                return

            for i in range(len(nums)):
                curr.append(nums[i])
                tmp = nums[:]
                tmp.pop(i)
                # print(f"i={i}, tmp={tmp}, curr={curr}")
                backtrack(i + 1, tmp, curr)
                curr.pop()

        backtrack(0, nums[:], [])

        return ans


class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        """
        個別の整数からなるの整数配列が指定されます。
        すべての順列を返します。

        バックトラッキングで再帰的に順列のリストを作成します。

        Time complexity: O(n!)
        Space complexity: O(n*n!)

        n は nums リストの長さです。

        #BackTracking

        Args:
            nums (list[int]): 個別の整数からなるの整数配列を指定します。

        Returns:
            list[list[int]]: 指定された整数配列の順列のリストを返します。
        """
        ans: list[list[int]] = []

        def backtrack(curr: list[int] = []):
            if len(nums) == len(curr):
                ans.append(curr[:])
                return

            for num in nums:
                if num not in curr:
                    curr.append(num)
                    print(f"curr={curr}")
                    backtrack(curr)
                    curr.pop()

        backtrack()

        return ans


sol = Solution()
print(sol.permute(nums=[1, 2, 3]))
