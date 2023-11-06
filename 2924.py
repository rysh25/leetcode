class Solution:
    def findChampion(self, n: int, edges: list[list[int]]) -> int:
        G: list[list[int]] = [[] for _ in range(n)]
        for edge in edges:
            G[edge[1]].append(edge[0])

        # print(f"G={G}")

        root: list[int] = []
        visited: list[bool] = [False] * n

        def dfs(v: int):
            # print(f"dfs: v={v}")
            if visited[v]:
                return
            if len(G[v]) == 0:
                # print(f"root: appended v={v}")
                root.append(v)

            visited[v] = True

            for nv in G[v]:
                dfs(nv)

        for i in range(len(G)):
            if visited[i]:
                continue
            dfs(i)

        # print(f"root={root}")

        return root[0] if len(root) == 1 else -1


sol = Solution()
print(sol.findChampion(n=3, edges=[[0, 1], [1, 2]]))
print(sol.findChampion(n=4, edges=[[0, 2], [1, 3], [1, 2]]))
