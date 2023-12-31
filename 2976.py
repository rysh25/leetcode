class Solution:
    def minimumCost(
        self,
        source: str,
        target: str,
        original: list[str],
        changed: list[str],
        cost: list[int],
    ) -> int:
        n = len(source)
        m = len(original)
        G: list[list[tuple[int, int]]] = [[] for _ in range(26)]

        for i in range(m):
            G[ord(original[i]) - ord("a")].append((ord(changed[i]) - ord("a"), cost[i]))

        visited: list[int] = [10**9 + 1] * 26

        def dfs(s: str, d: str, c: int, n: int) -> int:
            if n > 26:
                return 10**9 + 1
            if s == d:
                # print(f"found!: s={s}")
                return c
            curr = G[ord(s) - ord("a")]
            # print(f"s={s}, d={d}, curr.len={len(curr)}")

            ret = 10**9 + 1
            for nv in curr:
                nc = chr(nv[0] + ord("a"))
                if visited[nv[0]] < c:
                    continue
                # print(f"nc={nc}, c={nv[1]}")
                r = dfs(nc, d, nv[1] + c, n + 1)
                visited[ord(s) - ord("a")] = r
                ret = min(ret, r)

            return ret

        ans = 0

        cache: dict[str, int] = {}
        for i in range(n):
            visited: list[int] = [10**9 + 1] * 26
            # print(f"source={source[i]}, target={target[i]}")
            if source[i] in cache:
                ret = cache[source[i]]
            else:
                ret = dfs(source[i], target[i], 0, 0)
                cache[source[i]] = ret
            # print(f"source={source[i]}, target={target[i]}, cost={ret}")
            if ret >= 10**9 + 1:
                return -1
            ans += ret

        return ans


sol = Solution()
print(
    sol.minimumCost(
        source="abcd",
        target="acbe",
        original=["a", "b", "c", "c", "e", "d"],
        changed=["b", "c", "b", "e", "b", "e"],
        cost=[2, 5, 5, 1, 2, 20],
    )
)
print(
    sol.minimumCost(
        source="aaaa",
        target="bbbb",
        original=["a", "c"],
        changed=["c", "b"],
        cost=[1, 2],
    )
)
print(
    sol.minimumCost(
        source="abcd", target="abce", original=["a"], changed=["e"], cost=[10000]
    )
)
print(
    sol.minimumCost(
        source="aababdbddc",
        target="adcbbbcdba",
        original=["a", "d", "b", "a", "d", "c", "d", "b"],
        changed=["b", "a", "d", "c", "c", "a", "b", "a"],
        cost=[10, 6, 8, 3, 6, 10, 8, 6],
    )
)
