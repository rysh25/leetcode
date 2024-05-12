class Solution:
    def largestLocal(self, grid: list[list[int]]) -> list[list[int]]:
        """
        n x n の整数行列 grid が与えられます。

        次のようなサイズ (n - 2) x (n - 2) の整数行列 maxLocal を生成します。

        maxLocal[i][j] は、行 i + 1 と列 j + 1 を中心とするグリッド内の 3 x 3 行列の最大値に等しくなります。
        言い換えれば、グリッド内のすべての連続する 3 x 3 行列の最大値を見つけたいということです。

        生成された行列を返します。

        - Time complexity: O(n^2)
        - Space compleixty: O(n^2)

        Args:
            grid (list[list[int]]): n x n の整数行列

        Returns:
            list[list[int]]: 生成された行列を返します。
        """
        n = len(grid)

        max_local: list[list[int]] = [[0] * (n - 2) for _ in range(n - 2)]

        for i in range(n - 2):
            for j in range(n - 2):
                mx = 0
                for ki in range(3):
                    for kj in range(3):
                        mx = max(mx, grid[i + ki][j + kj])
                # print(f"i={i}, mx={mx}")
                max_local[i][j] = mx

        return max_local


sol = Solution()
print(sol.largestLocal(grid=[[9, 9, 8, 1], [5, 6, 2, 6], [8, 2, 6, 4], [6, 2, 2, 2]]))
print(
    sol.largestLocal(
        grid=[
            [1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1],
            [1, 1, 2, 1, 1],
            [1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1],
        ]
    )
)

print(sol.largestLocal(grid=[[2, 5, 5], [3, 2, 5], [1, 2, 3]]))
