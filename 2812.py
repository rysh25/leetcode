class Solution:
    def maximumSafenessFactor(self, grid: list[list[int]]) -> int:
        """
        n x n サイズのの2Dマトリックス grid が与えられます。
        ここで、(r, c)は以下を表します：

        - grid[r][c] = 1 の場合、そのセルには泥棒がいる
        - grid[r][c] = 0 の場合、そのセルは空いている

        あなたは最初にセル(0, 0)に位置しています。1回の移動で、泥棒がいるセルを含む隣接する任意のセルに移動できます。

        グリッド上の経路の安全性係数は、その経路上の任意のセルからグリッド内の泥棒までの最小マンハッタン距離として定義されます。

        セル(n - 1, n - 1)に至るすべての経路の最大安全性係数を返してください。

        セル(r, c)の隣接セルは、存在する場合、(r, c + 1)、(r, c - 1)、(r + 1, c)、(r - 1, c)のいずれかのセルです。

        2つのセル(a, b)と(x, y)の間のマンハッタン距離は|a - x| + |b - y|に等しく、ここで|val|はvalの絶対値を示します。


        初めに、BFS で、すべてのセルの安全性係を求める。
        その際、キューに初期値としてすべての泥棒の場所を詰めて、BFS を開始する。

        すべてのセルの安全係数がわかったら セル (0, 0) から安全係数が大きいセルを優先的に回わり、最初にセル(n-1, n-1)に
        たどり着いた時に、その経路の安全係数の最小値を最大安全性係数する。

        - Time complexty: O(n^2 log n)
        - Space complexity: O(n^2)

        #BFS

        Args:
            grid (list[list[int]]): n x n サイズのの2Dマトリックス

        Returns:
            int: セル (0, 0) から (n - 1, n - 1) に至るすべての経路の最大安全性係数を返してください。
        """
        import heapq
        from collections import deque

        n = len(grid)
        INF = 10**8 + 1
        safe_factors: list[list[int]] = [[INF] * n for _ in range(n)]

        dr: list[int] = [-1, 0, 1, 0]
        dc: list[int] = [0, 1, 0, -1]

        q: deque[tuple[int, int]] = deque()

        for r in range(n):
            for c in range(n):
                if grid[r][c] == 1:
                    safe_factors[r][c] = 0
                    q.append((r, c))

        while q:
            cr, cc = q.popleft()
            factor = safe_factors[cr][cc]
            # print(f"cr={cr}, cc={cc}")

            for di in range(4):
                nr, nc = cr + dr[di], cc + dc[di]
                # print(f"nr={nr}, nc={nc}")

                if nr < 0 or n <= nr or nc < 0 or n <= nc:
                    continue

                if grid[nr][nc] == 1:
                    continue

                if safe_factors[nr][nc] <= factor + 1:
                    continue

                safe_factors[nr][nc] = factor + 1
                q.append((nr, nc))

        # for r in range(n):
        #     print(safe_factors[r])

        visited: list[list[int]] = [[False] * n for _ in range(n)]
        pq: list[tuple[int, int, int]] = [(-safe_factors[0][0], 0, 0)]
        heapq.heapify(pq)

        ans = 0
        while pq:
            safe, r, c = heapq.heappop(pq)
            # print(f"safe={safe}, r={r}, c={c}")
            safe = -safe

            if r == n - 1 and c == n - 1:
                ans = safe
                break

            for di in range(4):
                nr, nc = r + dr[di], c + dc[di]

                if 0 <= nr < n and 0 <= nc < n and not visited[nr][nc]:
                    s = min(safe, safe_factors[nr][nc])
                    heapq.heappush(pq, (-s, nr, nc))
                    visited[nr][nc] = True

        return ans


sol = Solution()
print(sol.maximumSafenessFactor(grid=[[1, 0, 0], [0, 0, 0], [0, 0, 1]]))
print(sol.maximumSafenessFactor(grid=[[0, 0, 1], [0, 0, 0], [0, 0, 0]]))
print(
    sol.maximumSafenessFactor(
        grid=[[0, 0, 0, 1], [0, 0, 0, 0], [0, 0, 0, 0], [1, 0, 0, 0]]
    )
)
