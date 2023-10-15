class Solution:
    def constructProductMatrix(self, grid: list[list[int]]) -> list[list[int]]:
        """
        1次元の配列で考えて、前からと後ろからの累積積を事前に計算する。
        n x m の p を作成し、順番に現在のインデックスより前と後ろの積をかけた結果を入れる。

        - Time complexity: O(n * m)
        - Space complexity: O(n * m)

        Args:
            grid (list[list[int]]): n x n のグリッド

        Returns:
            list[list[int]]: p[i][j] について grid[i][j] 以外の要素の積
        """
        n = len(grid)
        m = len(grid[0])
        # print(f"grid={grid}")

        mod = 12345
        prefix, suffix = [1], [1]

        for i in range(n):
            for j in range(m):
                prefix.append((prefix[-1] * grid[i][j]) % mod)

        for i in reversed(range(n)):
            for j in reversed(range(m)):
                suffix.append((suffix[-1] * grid[i][j]) % mod)

        # print(f"prefix={prefix}, suffix={suffix}")

        p: list[list[int]] = [[0] * m for _ in range(n)]
        for i in range(n):
            for j in range(m):
                k = i * m + j
                # print(f"k={k}, -k - 2={-k - 2}")
                # print(f"prefix[k]={prefix[k]}, suffix[-k - 2]={suffix[-k - 2]}")
                p[i][j] = (prefix[k] * suffix[-k - 2]) % mod

        return p


sol = Solution()
print(sol.constructProductMatrix(grid=[[1, 2], [3, 4]]))
print(sol.constructProductMatrix(grid=[[12345], [2], [1]]))
