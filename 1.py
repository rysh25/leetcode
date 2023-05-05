import collections
from typing import DefaultDict, List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ans: DefaultDict[int, int] = collections.defaultdict(int)
        for i, num in enumerate(nums):
            if target - num in ans:
                return [ans[target - num], i]
            else:
                ans[num] = i
        return []


sol = Solution()
print(sol.twoSum(nums=[2, 7, 11, 15], target=9))
