class Solution:
    def maxPointsInsideSquare(self, points: list[list[int]], s: str) -> int:
        n = len(points)

        INF = 10**9 + 1
        tag_dist: list[list[int]] = [[INF] * 2 for _ in range(26)]

        # print(f"tag_dist={tag_dist}")

        for i in range(n):
            d = max(abs(points[i][0]), abs(points[i][1]))
            print(f"i={i}, t={s[i]}, d={d}")
            t = ord(s[i]) - ord("a")

            if tag_dist[t][0] > d:
                tag_dist[t][1] = tag_dist[t][0]
                tag_dist[t][0] = d
            elif tag_dist[t][1] > d:
                tag_dist[t][1] = d

        # print(f"tag_dist={tag_dist}")

        edge = INF
        for t in range(26):
            # print(f"t={chr(t + ord("a"))}, tag_dist[t][1]={tag_dist[t][1]}")
            edge = min(tag_dist[t][1] - 1, edge)

        # print(f"edge={edge}")

        ans = 0
        for i in range(n):
            d = max(abs(points[i][0]), abs(points[i][1]))

            if edge >= d:
                ans += 1

        return ans


sol = Solution()
# print(
#     sol.maxPointsInsideSquare(
#         points=[[2, 2], [-1, -2], [-4, 4], [-3, 1], [3, -3]], s="abdca"
#     )
# )
# print(sol.maxPointsInsideSquare(points=[[1, 1], [-2, -2], [-2, 2]], s="abb"))
# print(sol.maxPointsInsideSquare(points=[[1, 1], [-1, -1], [2, -2]], s="ccd"))
# print(
#     sol.maxPointsInsideSquare(points=[[-1, -4], [16, -8], [13, -3], [-12, 0]], s="abda")
# )
print(
    sol.maxPointsInsideSquare(
        points=[
            [60, 92],
            [-29, -8],
            [-24, 57],
            [-59, -99],
            [-93, -26],
            [-80, 35],
            [99, 34],
            [19, -99],
            [74, -94],
            [-8, -74],
        ],
        s="aefbgbihii",
    )
)
