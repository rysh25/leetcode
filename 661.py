class Solution:
    def imageSmoother(self, img: list[list[int]]) -> list[list[int]]:
        """
        画像スムーザーは、セルと周囲の 8 つのセルの平均 (つまり、青色のスムーザー内の 9 つのセルの平均) を切り捨てて、
        画像の各セルに適用できるサイズ 3 x 3 のフィルターです。
        セルの周囲のセルが 1 つ以上存在しない場合、そのセルは平均 (つまり、赤色スムーザー内の 4 つのセルの平均) には考慮されません。

        画像のグレースケールを表す m x n の整数行列 img が与えられた場合、その各セルにスムーザーを適用した後、画像を返します。

        - Time complexity: O(m * n)
        - Space complexity: O(m * n)

        Args:
            img (list[list[int]]): 画像のグレースケールを表す m x n の整数行列

        Returns:
            list[list[int]]: 各セルにスムーザーを適用した後、画像を返します。
        """
        n = len(img)
        m = len(img[0])
        ans: list[list[int]] = [[0] * m for _ in range(n)]

        dx = [1, 1, 1, 0, -1, -1, -1, 0]
        dy = [-1, 0, 1, 1, 1, 0, -1, -1]

        for i in range(n):
            for j in range(m):
                sum = img[i][j]
                count = 1
                for k in range(len(dx)):
                    if 0 <= i + dy[k] < n and 0 <= j + dx[k] < m:
                        sum += img[i + dy[k]][j + dx[k]]
                        count += 1
                ans[i][j] = sum // count
        return ans


sol = Solution()
print(sol.imageSmoother(img=[[1, 1, 1], [1, 0, 1], [1, 1, 1]]))
print(sol.imageSmoother(img=[[100, 200, 100], [200, 50, 200], [100, 200, 100]]))
