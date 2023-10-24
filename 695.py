class Solution:
    def maxAreaOfIsland(self, grid: list[list[int]]) -> int:
        """
        m x n の2次元のマトリックス grid が渡される。
        島は、土地を表す1の4方向に接続されるグループである。
        グリッドの4辺は水に囲まれているとみなす。
        島の面積は、島の値1のセルの数である。
        grid 内の島の面積の最大を返す。もし島がなければ0を返す。

        - Time complexity: O(mn)
        - Space complexity: O(mn)

        #DFS

        Args:
            grid (list[list[int]]): m x n の2次元のマトリックス

        Returns:
            int: grid 内の島の面積の最大を返す。
        """
        m = len(grid[0])
        n = len(grid)

        seen: list[list[bool]] = [[False] * m for _ in range(n)]

        dx = [0, 1, 0, -1]
        dy = [-1, 0, 1, 0]

        def dfs(x: int, y: int) -> int:
            if grid[y][x] != 1:
                return 0
            area = 1
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                seen[y][x] = True

                if 0 <= nx < m and 0 <= ny < n and not seen[ny][nx]:
                    area += dfs(nx, ny)
            return area

        ans = 0
        for y in range(n):
            for x in range(m):
                if not seen[y][x] and grid[y][x] == 1:
                    ans = max(ans, dfs(x, y))

        return ans


sol = Solution()
print(
    sol.maxAreaOfIsland(
        grid=[
            [0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
            [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
            [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0],
        ]
    )
)
print(sol.maxAreaOfIsland(grid=[[0, 0, 0, 0, 0, 0, 0, 0]]))
