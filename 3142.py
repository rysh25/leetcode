class Solution:
    def satisfiesConditions(self, grid: list[list[int]]) -> bool:
        m = len(grid[0])
        n = len(grid)
        for i in range(n - 1):
            for j in range(m):
                if grid[i][j] != grid[i + 1][j]:
                    return False
        for j in range(m - 1):
            for i in range(n):
                if grid[i][j] == grid[i][j + 1]:
                    return False
        return True


sol = Solution()
print(sol.satisfiesConditions(grid=[[1, 0, 2], [1, 0, 2]]))
print(sol.satisfiesConditions(grid=[[1, 1, 1], [0, 0, 0]]))
print(sol.satisfiesConditions(grid=[[1], [2], [3]]))
