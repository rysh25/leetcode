class Solution:
    def findMissingAndRepeatedValues(self, grid: list[list[int]]) -> list[int]:
        n = len(grid)
        freq: list[int] = [0] * (n * n + 1)
        for i in range(n):
            for j in range(n):
                freq[grid[i][j]] += 1

        ans: list[int] = [0] * 2
        for i in range(1, len(freq)):
            # print(f"i={i}")
            if freq[i] == 0:
                ans[1] = i
            elif freq[i] == 2:
                ans[0] = i
        return ans


sol = Solution()
print(sol.findMissingAndRepeatedValues(grid=[[1, 3], [2, 2]]))
print(sol.findMissingAndRepeatedValues(grid=[[9, 1, 7], [8, 9, 2], [3, 4, 6]]))
