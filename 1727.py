class Solution:
    def largestSubmatrix(self, matrix: list[list[int]]) -> int:
        """
        サイズ m x n のバイナリ行列が与えられ、行列の列を任意の順序で並べ替えることができます。

        列を最適に並べ替えた後、部分行列のすべての要素が 1 になる行列内の最大の部分行列の面積を返します。


        事前に各セルの列ごとに何行1が続いているかを計算します。
        その後、行ごとに事前解散した値をソートし、全セルについて、面接を求め最大の面積を見つけます。


        - Time complexity: O(m*n log n)
        - Space complexity: O(nm)


        Args:
            matrix (list[list[int]]): サイズ m x n のバイナリ行列

        Returns:
            int: 部分行列のすべての要素が 1 になる行列内の最大の部分行列の面積を返します。
        """
        m = len(matrix)
        n = len(matrix[0])
        # print(f"matrix={matrix}")

        prefix_streak_row: list[list[int]] = [[0] * n for _ in range(m)]
        for c in range(n):
            for r in range(m):
                if matrix[r][c] == 1:
                    if r == 0:
                        prefix_streak_row[r][c] = 1
                    else:
                        prefix_streak_row[r][c] = prefix_streak_row[r - 1][c] + 1

        # print(f"prefix_streak_row={prefix_streak_row}")

        ans = 0
        for r in range(m):
            prefix_streak_row[r].sort()
            for c in range(n):
                if prefix_streak_row[r][c] > 0:
                    ans = max(ans, (n - c) * prefix_streak_row[r][c])

        return ans


sol = Solution()
print(sol.largestSubmatrix(matrix=[[0, 0, 1], [1, 1, 1], [1, 0, 1]]))
print(sol.largestSubmatrix(matrix=[[1, 0, 1, 0, 1]]))
print(sol.largestSubmatrix(matrix=[[1, 1, 0], [1, 0, 1]]))
