class Solution:
    def matrixScore(self, grid: list[list[int]]) -> int:
        """
        m x n のバイナリ行列 grid が与えられます。

        移動は、任意の行または列を選択し、その行または列の各値を切り替えることで構成されます。

        行列の各行は 2 進数として解釈され、行列のスコアはこれらの数値の合計になります。

        任意の数の手（ゼロ手も含む）を行った後、可能な限り最高のスコアを返します。

        - Time complexty: O(mn)
        - Space complexty: O(1)

        #Greedy

        Args:
            grid (list[list[int]]): m x n のバイナリ行列

        Returns:
            int: 任意の数の手（ゼロ手も含む）を行った後、可能な限り最高のスコアを返します。
        """
        m = len(grid[0])
        n = len(grid)

        for i in range(n):
            # print(f"{grid[i]}")
            if grid[i][0] == 0:
                for j in range(m):
                    grid[i][j] ^= 0 ^ 1
        # print("")

        # for i in range(n):
        #     print(f"{grid[i]}")
        # print("")

        for j in range(m):
            count_1 = 0
            for i in range(n):
                if grid[i][j] == 1:
                    count_1 += 1

            if count_1 <= n / 2:
                for i in range(n):
                    grid[i][j] ^= 0 ^ 1

        ans = 0
        for i in range(n):
            x = 1
            # print(f"{grid[i]}")
            for j in range(m - 1, -1, -1):
                if grid[i][j] == 1:
                    ans += x
                x *= 2

        return ans


sol = Solution()
print(sol.matrixScore(grid=[[0, 0, 1, 1], [1, 0, 1, 0], [1, 1, 0, 0]]))
print(sol.matrixScore(grid=[[0]]))
