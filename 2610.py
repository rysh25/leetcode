class Solution:
    def findMatrix(self, nums: list[int]) -> list[list[int]]:
        ans: list[list[int]] = []
        current_row: set[int] = set()
        used_index: set[int] = set()

        while True:
            i = 0
            current_row = set()
            while i < len(nums):
                if i not in used_index and nums[i] not in current_row:
                    current_row.add(nums[i])
                    used_index.add(i)
                i += 1
            ans.append(list(current_row))

            if len(used_index) == len(nums):
                break
        return ans


sol = Solution()
print(sol.findMatrix(nums=[1, 3, 4, 1, 2, 3, 1]))
print(sol.findMatrix(nums=[1, 2, 3, 4]))
