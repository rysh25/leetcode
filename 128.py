from typing import List, Set


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s: Set[int] = set(nums)

        ans = 0
        for num in nums:
            if num - 1 not in s:
                length = 1
                while num + length in s:
                    length += 1
                ans = max(ans, length)
        return ans


sol = Solution()
print(sol.longestConsecutive(nums=[100, 4, 200, 1, 3, 2]))
print(sol.longestConsecutive(nums=[0, 3, 7, 2, 5, 8, 4, 6, 0, 1]))
