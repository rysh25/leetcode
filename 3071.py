class Solution:
    def minimumOperationsToWriteY(self, grid: list[list[int]]) -> int:
        n = len(grid)

        # print(f"grid={grid}")

        def is_y(r: int, c: int) -> bool:
            if c < n // 2 and r == c:
                return True
            elif c > n // 2 and r == n - c - 1:
                return True
            elif c == n // 2 and r >= n // 2:
                return True
            return False

        y_count: list[int] = [0, 0, 0]
        not_y_count: list[int] = [0, 0, 0]

        for r in range(n):
            for c in range(n):
                if is_y(r, c):
                    y_count[grid[r][c]] += 1
                else:
                    not_y_count[grid[r][c]] += 1

        y_n = (n // 2 * 3) + 1
        not_y_n = n * n - y_n
        ans = 10**9 + 1
        for i in range(3):
            y = y_n - y_count[i]

            for j in range(3):
                if j == i:
                    continue
                not_y = not_y_n - not_y_count[j]

                ans = min(ans, y + not_y)
        # print(f"y_count={y_count}")
        # print(f"not_y_count={not_y_count}")

        return ans


sol = Solution()
print(sol.minimumOperationsToWriteY(grid=[[1, 2, 2], [1, 1, 0], [0, 1, 0]]))
print(
    sol.minimumOperationsToWriteY(
        grid=[
            [0, 1, 0, 1, 0],
            [2, 1, 0, 1, 2],
            [2, 2, 2, 0, 1],
            [2, 2, 2, 2, 2],
            [2, 1, 2, 2, 2],
        ]
    )
)
