from collections import defaultdict


class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        """
        整数配列 nums と、整数 target が与えられる。
        足すと target になる2つのインデックスを返します。

        nums 配列の各値を入れるディクショナリーを作る
        nums 配列をループしながら、target から現在の値を引いた値がディクショナリーに
        存在するか調べ、あれば、その組み合わせを返して終了。なければディクショナリーに値を設定し
        次のループに進む

        Time complexity: O(N)
        Space complexity: O(N)

        #Array
        """
        ans: defaultdict[int, int] = defaultdict(int)
        for i, num in enumerate(nums):
            if target - num in ans:
                return [ans[target - num], i]
            else:
                ans[num] = i
        return []


sol = Solution()
print(sol.twoSum(nums=[2, 7, 11, 15], target=9))
