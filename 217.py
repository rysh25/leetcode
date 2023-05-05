from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(nums) != len(set(nums))


sol = Solution()
print(sol.containsDuplicate(nums=[1, 2, 3, 4]))
