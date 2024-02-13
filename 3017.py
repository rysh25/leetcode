class Solution:
    def countOfPairs(self, n: int, x: int, y: int) -> list[int]:
        from collections import deque

        ans: list[int] = [0] * n

        g: list[list[int]] = [[] for _ in range(n)]

        for i in range(n - 1):
            g[i].append(i + 1)
            g[i + 1].append(i)

        g[x - 1].append(y - 1)
        g[y - 1].append(x - 1)

        memo: list[int] = [-1] * n

        # print(f"g={g}")

        def bfs(i: int, visited: list[bool]):
            # print(f"bfs: i={i}")
            q: deque[tuple[int, int]] = deque()  # (index, depth)

            q.append((i, 0))

            while q:
                ci, cd = q.popleft()

                # print(f"ci={ci}, cd={cd}")

                if visited[ci]:
                    continue

                visited[ci] = True

                if cd > n:
                    continue

                if cd > 0:
                    ans[cd - 1] += 1

                for ni in g[ci]:
                    q.append((ni, cd + 1))

            return

        for i in range(n):
            bfs(i, [False] * n)

        return ans


sol = Solution()
print(sol.countOfPairs(n=3, x=1, y=3))
print(sol.countOfPairs(n=5, x=2, y=4))
print(sol.countOfPairs(n=4, x=1, y=1))
