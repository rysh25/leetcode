class Solution:
    def countSubmatrices(self, grid: list[list[int]], k: int) -> int:
        m = len(grid[0])
        n = len(grid)
        sum: list[list[int]] = [[0] * (m + 1) for _ in range(n + 1)]

        # print(f"grid={grid}")

        for i in range(n):
            for j in range(m):
                sum[i + 1][j + 1] = grid[i][j]

        for i in range(n):
            for j in range(m):
                sum[i + 1][j + 1] += sum[i + 1][j]

        for j in range(m):
            for i in range(n):
                sum[i + 1][j + 1] += sum[i][j + 1]

        # print(f"sum={sum}")

        ans = 0
        for i in range(n):
            for j in range(m):
                if sum[i + 1][j + 1] <= k:
                    ans += 1
        return ans


sol = Solution()
print(sol.countSubmatrices(grid=[[7, 6, 3], [6, 6, 1]], k=18))
print(sol.countSubmatrices(grid=[[7, 2, 9], [1, 5, 0], [2, 6, 6]], k=20))
