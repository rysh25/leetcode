class Solution:
    def minFallingPathSum(self, matrix: list[list[int]]) -> int:
        """
        整数行列の n x n 配列を渡されます。
        行列を通過するすべての下降パスの最小合計を返します。

        下降パスは最初の行の任意の要素から始まり、真下または斜め左/右にある次の行の要素を選択します。
        具体的には、位置 (row,col) の次の要素は、(row + 1,col - 1)、(row + 1,col)、または (row + 1,col + 1) になります。


        DP を行う。
        dp テーブルを用意し、dp[i][j] に、i行目のi列目からの最小値を記録する。
        dp[-1][j] に、matrix[-1][j] を初期値とする。
        dp[i][j] に min(dp[i+1][j-1], dp[i+1][j], dp[i+1][j-1]) + matrix[i][j] を最小行から順番に記録していく。
        実際には、0列目と最終列目の場合、下の行の j-1 か、j+1 が存在しないため、番兵として余分に2列分を dp テーブルに用意しておく。

        #DP

        - Time complexity: O(n^2)
        - Space complexity: O(n^2)

        Args:
            matrix (list[list[int]]): 整数行列の n x n 配列

        Returns:
            int: 行列を通過するすべての下降パスの最小合計を返します。
        """
        INF = 10**9 + 1
        n = len(matrix)
        dp: list[list[int]] = [[INF] * (n + 2) for _ in range(n)]

        for j in range(n):
            dp[-1][j + 1] = matrix[-1][j]

        for i in range(1, n):
            for j in range(1, n + 1):
                dp[n - i - 1][j] = (
                    min(dp[n - i][j - 1], dp[n - i][j], dp[n - i][j + 1])
                    + matrix[n - i - 1][j - 1]
                )

        # print(f"dp={dp}")

        return min(dp[0])


sol = Solution()
print(sol.minFallingPathSum(matrix=[[2, 1, 3], [6, 5, 4], [7, 8, 9]]))
print(sol.minFallingPathSum(matrix=[[-19, 57], [-40, -5]]))
