class Solution:
    def transpose(self, matrix: list[list[int]]) -> list[list[int]]:
        """
        2次元整数配列 matrx を指定すると、matrix の転置を返します。

        Time complexity: O(n * m)
        Space complexity: O(n * m)

        Args:
            matrix (list[list[int]]): 2次元整数配列

        Returns:
            list[list[int]]: matrix の転置を返します。
        """
        m = len(matrix)
        n = len(matrix[0])
        ans: list[list[int]] = [[0] * m for _ in range(n)]

        for r in range(m):
            for c in range(n):
                ans[c][r] = matrix[r][c]
        return ans


sol = Solution()
print(sol.transpose(matrix=[[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
print(sol.transpose(matrix=[[1, 2, 3], [4, 5, 6]]))
