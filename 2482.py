class Solution:
    def onesMinusZeros(self, grid: list[list[int]]) -> list[list[int]]:
        """
        0 インデックスの m x n のバイナリ行列 grid が与えられる。

        0 インデックスの m x n 差分行列 diff は以下の手順で作成される：

        - i行目のonesの数をonesRowiとする。
        - j列目の1の数をonesColjとする。
        - i行目の0の数をzerosRowiとする。
        - j列目の0の数をzerosColjとする。
        - diff[i][j] = onesRowi + onesColj - zerosRowi - zerosColj

        差分行列 diff を返す

        - Time complexity: O(m * n)
        - Space complexity: O(m + n)

        Args:
            grid (list[list[int]]):  m x n のバイナリ行列

        Returns:
            list[list[int]]: 差分行列 diff を返す
        """
        m = len(grid[0])
        n = len(grid)
        sum_rows: list[int] = [0] * n
        sum_cols: list[int] = [0] * m

        for i in range(n):
            for j in range(m):
                sum_rows[i] += grid[i][j]

        for j in range(m):
            for i in range(n):
                sum_cols[j] += grid[i][j]

        # print(f"sum_rows={sum_rows}")
        # print(f"sum_cols={sum_cols}")

        diff: list[list[int]] = [[0] * m for _ in range(n)]

        for i in range(n):
            for j in range(m):
                diff[i][j] = (
                    sum_rows[i] + sum_cols[j] - (m - sum_rows[i]) - (n - sum_cols[j])
                )

        return diff


sol = Solution()
print(sol.onesMinusZeros(grid=[[0, 1, 1], [1, 0, 1], [0, 0, 1]]))
print(sol.onesMinusZeros(grid=[[1, 1, 1], [1, 1, 1]]))
