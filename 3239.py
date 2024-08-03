class Solution:
    def minFlips(self, grid: list[list[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        ans = 10**9 + 1

        flips = 0
        for i in range(m):
            for j in range(n // 2):
                if grid[i][j] != grid[i][n - j - 1]:
                    # print(f"flip: i={i}, j={j}")
                    flips += 1

        # print(f"flips={flips}")
        ans = min(ans, flips)

        flips = 0
        for j in range(n):
            for i in range(m // 2):
                if grid[i][j] != grid[m - i - 1][j]:
                    # print(f"flip: i={i}, j={j}")
                    flips += 1

        # print(f"flips={flips}")
        ans = min(ans, flips)

        return ans


sol = Solution()
print(sol.minFlips(grid=[[1, 0, 0], [0, 0, 0], [0, 0, 1]]))
print(sol.minFlips(grid=[[0, 1], [0, 1], [0, 0]]))
print(sol.minFlips(grid=[[1], [0]]))
