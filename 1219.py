class Solution:
    def getMaximumGold(self, grid: list[list[int]]) -> int:
        """
        サイズが m x n の金鉱の grid が、それぞれのセルにはそのセルにある金の量を表す整数が入っています。空の場合は0です。

        以下の条件のもとで集められる最大の金の量を返してください：

        - あなたがセルにいるたびに、そのセルにあるすべての金を集めます。
        - あなたの位置から、左、右、上、または下に1歩進むことができます。
        - 同じセルを2回訪れることはできません。
        - 金が0のセルには訪れないでください。
        - グリッド内の金がある任意の位置から金を集め始め、終了することができます。

        - Time complexity: O(m * n)
        - Space complexity: O(m * n)

        #DFS
        #Backgracking

        Args:
            grid (list[list[int]]): サイズが m x n の金鉱

        Returns:
            int: 最大の金の量を返してください
        """
        m = len(grid[0])
        n = len(grid)

        visited: list[list[bool]] = [[False] * m for _ in range(n)]

        dx: list[int] = [0, 1, 0, -1]
        dy: list[int] = [-1, 0, 1, 0]

        ans = 0

        def dfs(x: int, y: int, g: int):
            cg = grid[y][x]
            nonlocal ans
            ans = max(ans, g + cg)

            if cg == 0:
                return

            visited[y][x] = True

            for di in range(4):
                nx, ny = x + dx[di], y + dy[di]

                if ny < 0 or n <= ny or nx < 0 or m <= nx:
                    continue
                if visited[ny][nx]:
                    continue

                dfs(nx, ny, g + cg)

            visited[y][x] = False
            return

        for y in range(n):
            for x in range(m):
                if visited[y][x]:
                    continue
                dfs(x, y, 0)

        return ans


sol = Solution()
print(sol.getMaximumGold(grid=[[0, 6, 0], [5, 8, 7], [0, 9, 0]]))
print(sol.getMaximumGold(grid=[[1, 0, 7], [2, 0, 6], [3, 4, 5], [0, 3, 0], [9, 0, 20]]))
print(
    sol.getMaximumGold(
        grid=[
            [1, 0, 7, 0, 0, 0],
            [2, 0, 6, 0, 1, 0],
            [3, 5, 6, 7, 4, 2],
            [4, 3, 1, 0, 2, 0],
            [3, 0, 5, 0, 20, 0],
        ]
    )
)  # 64
