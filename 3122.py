class Solution:
    def minimumOperations(self, grid: list[list[int]]) -> int:

        m = len(grid[0])
        n = len(grid)

        freq: list[list[int]] = [[0] * 10 for _ in range(m)]

        for j in range(m):
            for i in range(n):
                freq[j][grid[i][j]] += 1

        # print(f"freq={freq}")

        dp: list[list[int]] = [[0] * 10 for _ in range(m)]

        for j in range(m):
            for num in range(10):
                x = n - freq[j][num]

                if j == 0:
                    # print(f"j={j}, num={num}, x={x}")
                    dp[j][num] = x
                else:
                    mn = j * n
                    for num2 in range(10):
                        if num != num2:
                            mn = min(mn, dp[j - 1][num2])
                    # print(f"n={n}, j={j}, num={num}, x={x}, mn={mn}")
                    dp[j][num] = mn + x

        # print(f"dp={dp}")

        return min(dp[m - 1])


sol = Solution()
print(sol.minimumOperations(grid=[[1, 0, 2], [1, 0, 2]]))
print(sol.minimumOperations(grid=[[1, 1, 1], [0, 0, 0]]))
print(sol.minimumOperations(grid=[[1], [2], [3]]))
print(sol.minimumOperations(grid=[[0, 6, 2], [9, 0, 9], [4, 9, 6]]))  # 6
print(
    sol.minimumOperations(
        grid=[[4, 5, 0, 1], [1, 9, 0, 8], [2, 2, 5, 3], [2, 0, 9, 3]]
    )  # 9
)
print(
    sol.minimumOperations(
        grid=[
            [0, 0, 3, 2, 2, 2],
            [6, 3, 8, 8, 2, 7],
            [1, 4, 5, 4, 3, 0],
            [6, 4, 2, 9, 2, 5],
            [9, 3, 7, 3, 9, 3],
            [5, 3, 5, 2, 0, 3],
        ]
    )  # 23
)

print(
    sol.minimumOperations(
        grid=[
            [0, 1],
            [9, 1],
            [0, 3],
            [0, 5],
            [1, 8],
            [4, 6],
            [0, 2],
            [1, 3],
            [0, 2],
            [1, 9],
        ]
    )
)  # 13
