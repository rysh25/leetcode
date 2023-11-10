class Solution:
    def restoreArray(self, adjacentPairs: list[list[int]]) -> list[int]:
        """
        n 個の一意の要素で構成される整数配列 nums がありますが、それを忘れてしまいました。
        ただし、隣接する要素のすべてのペアは nums で記憶されます。

        サイズ n - 1 の 2D 整数配列隣接ペアが与えられます。
        ここで、各隣接ペア[i] = [ui, vi] は、要素 ui と vi が nums で隣接していることを示します。

        要素 nums[i] と nums[i+1] のすべての隣接するペアが [nums[i], nums[i+1]] または [nums[i+1], nums] として隣接ペアに存在することが保証されます。
        ペアは任意の順序で表示できます。

        元の配列 nums を返します。 複数の解がある場合は、いずれかを返します。


        隣接ペアから、グラフを作成しする。
        隣接ノードがの数が1のものから、DFS で隣接ノードを順番にトラバースしながら、ノードの配列を作成する。

        - Time complxity: O(n)
        - Time complxity: O(n)

        #DFS

        Args:
            adjacentPairs (list[list[int]]): サイズ n - 1 の 2D 整数配列隣接ペアが与えられます。

        Returns:
            list[int]: 元の配列 nums を返します。
        """
        n = len(adjacentPairs) + 1
        G: list[list[int]] = [[] for _ in range(n)]

        d: dict[int, int] = {}
        dr: dict[int, int] = {}
        i = 0
        for pair in adjacentPairs:
            p0v = 0
            p1v = 0
            if pair[0] not in d:
                d[pair[0]] = i
                dr[i] = pair[0]
                i += 1
            if pair[1] not in d:
                d[pair[1]] = i
                dr[i] = pair[1]
                i += 1

            p0v = d[pair[0]]
            p1v = d[pair[1]]
            G[p0v].append((p1v))
            G[p1v].append((p0v))
        # print(f"G={G}")
        # print(f"d={d}", f"dr={dr}")
        start_v = -1
        for i in range(len(G)):
            if len(G[i]) == 1:
                start_v = i

        seen: list[int] = [False] * n

        ans: list[int] = []

        def dfs(v: int):
            ans.append(dr[v])
            seen[v] = True

            for nv in G[v]:
                if seen[nv]:
                    continue
                dfs(nv)

        # print(f"start_v={start_v}, dr[start_v]={dr[start_v]}")

        dfs(start_v)

        return ans


sol = Solution()
print(sol.restoreArray(adjacentPairs=[[2, 1], [3, 4], [3, 2]]))
print(sol.restoreArray(adjacentPairs=[[4, -2], [1, 4], [-3, 1]]))
print(sol.restoreArray(adjacentPairs=[[100000, -100000]]))
