from collections import defaultdict


class Solution:
    def findDiagonalOrder(self, nums: list[list[int]]) -> list[int]:
        d: defaultdict[int, list[int]] = defaultdict(list)
        for i in range(len(nums)):
            for j in range(len(nums[i])):
                d[i + j].append(nums[i][j])
        return [v for k in d.keys() for v in reversed(d[k])]


sol = Solution()
print(sol.findDiagonalOrder(nums=[[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
print(
    sol.findDiagonalOrder(
        nums=[[1, 2, 3, 4, 5], [6, 7], [8], [9, 10, 11], [12, 13, 14, 15, 16]]
    )
)
