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


        バス停分の最小の乗車回数を保持するリストを用意する。
        まず、source のバス停を0に設定する

        次にルート単位に次の処理を行う。
        1. そのルート内のバス停までの乗車回数の最小値を取得する。
        2. そのルート内のバス停を、上で取得したバス停と同じルートに存在すると判断し、最小乗車回数がより大きいなら最小値+1で更新する。
        すべてのルートが更新ができなくなるまで繰り返す。


        - Time complexity: O(numberOfRoutes * numberOfStops)
        - Space complexity: O(maxStop)

        #Graph

        Args:
            routes (list[list[int]]): バス ルートを表す配列
            source (int): スタート
            target (int): 行き先

        Returns:
            int: ソースからターゲットまで移動するために乗らなければならないバスの最小数を返します。
        """
        if source == target:
            return 0

        max_stop = max(max(route) for route in routes)
        if max_stop < target:
            return -1

        INF = 10**9 + 1
        min_buses_to_reach = [INF] * (max_stop + 1)
        min_buses_to_reach[source] = 0

        updated = True
        while updated:
            updated = False
            for route in routes:
                mini = INF
                for stop in route:
                    mini = min(mini, min_buses_to_reach[stop])
                mini += 1
                for stop in route:
                    if min_buses_to_reach[stop] > mini:
                        min_buses_to_reach[stop] = mini
                        updated = True

        return min_buses_to_reach[target] if min_buses_to_reach[target] < INF else -1


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
