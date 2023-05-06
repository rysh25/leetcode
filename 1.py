import collections
from typing import DefaultDict, List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        nums 配列の各値を入れるディクショナリーを作る
        nums 配列をループしながら、target から現在の値を引いた値がディクショナリーに
        存在するか調べ、あれば、その組み合わせを返して終了。なければディクショナリーに値を設定し
        次のループに進む

        Time complexity: O(N)
        Space complexity: O(N)
        """
        ans: DefaultDict[int, int] = collections.defaultdict(int)
        for i, num in enumerate(nums):
            if target - num in ans:
                return [ans[target - num], i]
            else:
                ans[num] = i
        return []


sol = Solution()
print(sol.twoSum(nums=[2, 7, 11, 15], target=9))
