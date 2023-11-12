from collections import defaultdict, deque


class Solution:
    def numBusesToDestination(
        self, routes: list[list[int]], source: int, target: int
    ) -> int:
        """
        バス ルートを表す配列 route が与えられます。
        routes[i] は、i 番目のバスが永久に繰り返すバス ルートです。

        sourcee のバス停からスタートし (最初はどのバスにも乗っていません)、
        traget のバス停に行きたいとします。 バス停間の移動はバスのみとなります。

        ソースからターゲットまで移動するために乗らなければならないバスの最小数を返します。
        不可能な場合は -1 を返します。

        #Graph

        Args:
            routes (list[list[int]]): バス ルートを表す配列
            source (int): スタート
            target (int): 行き先

        Returns:
            int: ソースからターゲットまで移動するために乗らなければならないバスの最小数を返します。
        """
        num_routes = len(routes)
        G: list[set[int]] = [set() for _ in range(num_routes)]
        stop_route_map: defaultdict[int, set[int]] = defaultdict(set)
        source_routes: set[int] = set()
        target_routes: set[int] = set()

        if source == target:
            return 0

        for i, route in enumerate(routes):
            for bus in route:
                stop_route_map[bus].add(i)
                if bus == source:
                    source_routes.add(i)
                if bus == target:
                    target_routes.add(i)

        # print(f"stop_route_map: {stop_route_map}")

        for i, route in enumerate(routes):
            for bus in route:
                for j in stop_route_map[bus]:
                    if i == j:
                        continue
                    G[i].add(j)
                    G[j].add(i)
        # print(f"G: {G}")
        # print(f"source_routes: {source_routes}")
        # print(f"target_routes: {target_routes}")

        INF = 10**9 + 1

        def bfs(v: int) -> int:
            seen = [False] * num_routes
            # print(f"call bfs: s={s}")

            q: deque[tuple[int, int]] = deque()
            q.append((v, 1))

            ret = INF

            while q:
                cv, n = q.pop()
                # print(f"cv={cv}, n={n}")

                if cv in target_routes:
                    ret = min(ret, n)

                seen[cv] = True

                for nv in G[cv]:
                    if seen[nv]:
                        continue
                    q.append((nv, n + 1))
            return ret

        ans = INF
        for s in source_routes:
            ans = min(ans, bfs(s))

        return ans if ans < INF else -1


sol = Solution()
print(sol.numBusesToDestination(routes=[[1, 2, 7], [3, 6, 7]], source=1, target=6))
print(
    sol.numBusesToDestination(
        routes=[[7, 12], [4, 5, 15], [6], [15, 19], [9, 12, 13]], source=15, target=12
    )
)

print(
    sol.numBusesToDestination(
        routes=[
            [1, 9, 12, 20, 23, 24, 35, 38],
            [10, 21, 24, 31, 32, 34, 37, 38, 43],
            [10, 19, 28, 37],
            [8],
            [14, 19],
            [11, 17, 23, 31, 41, 43, 44],
            [21, 26, 29, 33],
            [5, 11, 33, 41],
            [4, 5, 8, 9, 24, 44],
        ],
        source=37,
        target=28,
    )
)  # 1

print(
    sol.numBusesToDestination(
        routes=[[1, 7], [3, 5]],
        source=5,
        target=5,
    )
)  # 0
