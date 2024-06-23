class Solution:
    def minimumArea(self, grid: list[list[int]]) -> int:
        min_x, max_x = 1001001001, 0
        min_y, max_y = 1001001001, 0

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 1:
                    min_x = min(min_x, j)
                    max_x = max(max_x, j)
                    min_y = min(min_y, i)
                    max_y = max(max_y, i)

        return (max_x - min_x + 1) * (max_y - min_y + 1)


sol = Solution()
print(sol.minimumArea(grid=[[0, 1, 0], [1, 0, 1]]))
print(sol.minimumArea(grid=[[0, 0], [1, 0]]))
