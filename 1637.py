class Solution:
    def maxWidthOfVerticalArea(self, points: list[list[int]]) -> int:
        """
        2次元平面上に n 個の点 (points[i] = [xi, yi]) がある場合、領域内に点が存在しないように 2 点間の最も広い垂直領域を返します。

        垂直領域は、y 軸に沿って無限に広がる固定幅の領域 (つまり、無限の高さ) です。 最も広い垂直領域は、最大幅を持つ領域です。

        垂直領域の端にある点は、その領域に含まれるとはみなされないことに注意してください。

        - Time complexity: O(n log n)
        - Space complexity: O(1)

        Args:
            points (list[list[int]]): 2次元平面上に n 個の点を表す配列

        Returns:
            int: 領域内に点が存在しないように 2 点間の最も広い垂直領域を返します。
        """
        points.sort()

        ans = 0
        for i in range(len(points) - 1):
            ans = max(ans, points[i + 1][0] - points[i][0])

        return ans


sol = Solution()
print(sol.maxWidthOfVerticalArea(points=[[8, 7], [9, 9], [7, 4], [9, 7]]))
print(
    sol.maxWidthOfVerticalArea(points=[[3, 1], [9, 0], [1, 0], [1, 4], [5, 3], [8, 8]])
)
