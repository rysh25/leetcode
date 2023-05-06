from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        """
        各数字が配列の中に2回以上出てくるか調べるために、nums を set に入れて、
        長さが元と変わっているかを調べる。

        Time complexity: O(N)
        Space complexity: O(N)
        """
        return len(nums) != len(set(nums))


sol = Solution()
print(sol.containsDuplicate(nums=[1, 2, 3, 4]))
