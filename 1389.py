class Solution:
    def createTargetArray(self, nums: list[int], index: list[int]) -> list[int]:
        """
        nums と index の2つの整数配列が指定されます。

        次のルールに従って、target 配列を作成し返します。

        - 最初は target 配列は空です。
        - 左から右に nums[i] と Index[i] を読み取り、target 配列の index[i] に値 nums[i] を挿入します。
        - nums と index に読み取る要素がなくなるまで、前の手順を繰り返します。

        Time complexity: O(n^2)
        Space complexity: O(n)

        Args:
            nums (list[int]): nums 配列を指定します。
            index (list[int]): index 配列を指定します。

        Returns:
            list[int]: 作成した target 配列を返します。
        """
        target: list[int] = []

        for num, i in zip(nums, index):
            target.insert(i, num)

        return target


sol = Solution()
print(sol.createTargetArray(nums=[0, 1, 2, 3, 4], index=[0, 1, 2, 2, 1]))
