class Solution:
    def minTimeToVisitAllPoints(self, points: list[list[int]]) -> int:
        """
        2次元平面上で、n個のポイントがあります。
        すべてのポイントを訪問する最小時間を返します。

        1行間の移動距離は、縦と横の移動距離の長い方になります。

        - Time complexity: O(n)
        - Space complexity: O(1)

        n は、points リストの長さです。

        Args:
            points (list[list[int]]): ポイントの座標 [x_i, y_i] のリストを指定します。

        Returns:
            int: 最小時間を返します。
        """
        if not points:
            return 0

        ans = 0.0
        prev = points[0]
        for i in range(1, len(points)):
            sec = max(abs(prev[0] - points[i][0]), abs(prev[1] - points[i][1]))
            print(f"prev={prev}, points[{i}]={points[i]}, sec={sec}")
            ans += sec
            prev = points[i]

        return int(ans)


sol = Solution()
print(sol.minTimeToVisitAllPoints(points=[[1, 1], [3, 4], [-1, 0]]))
print(sol.minTimeToVisitAllPoints(points=[[3, 2], [-2, 2]]))
