class Solution:
    def maximumScoreAfterOperations(
        self, edges: list[list[int]], values: list[int]
    ) -> int:
        n = len(values)
        G: list[list[int]] = [[] for _ in range(n)]
        for edge in edges:
            G[edge[0]].append(edge[1])
            G[edge[1]].append(edge[2])

        # print(f"G={G}")

        total = sum(values[1:])

        def dfs(v: int) -> int:
            print(f"dfs: v={v}")

            count = 0
            for nv in G[v]:
                count += dfs(nv)

            print(f"return count={count}, values[v]={values[v]}")
            return max(count, values[v])

        count = dfs(0)
        print(f"totoal={total}, count={count}")
        return max(count, total)


sol = Solution()
print(
    sol.maximumScoreAfterOperations(
        edges=[[0, 1], [0, 2], [0, 3], [2, 4], [4, 5]], values=[5, 2, 5, 2, 1, 1]
    )
)
# print(
#     sol.maximumScoreAfterOperations(
#         edges=[[0, 1], [0, 2], [1, 3], [1, 4], [2, 5], [2, 6]],
#         values=[20, 10, 9, 7, 4, 3, 5],
#     )
# )
