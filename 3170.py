class Solution:
    def clearStars(self, s: str) -> str:
        print(f"s={s}")
        import heapq

        ast_i = 0
        small: list[tuple[str, int]] = []
        heapq.heapify(small)

        deleted_i: set[int] = set()

        while True:
            while ast_i < len(s) and s[ast_i] != "*":
                heapq.heappush(small, (s[ast_i], -ast_i))
                ast_i += 1

            if ast_i >= len(s):
                break

            # print(f"ast_i={ast_i}, len(small)={len(small)}")
            x = heapq.heappop(small)
            deleted_i.add(-x[1])
            ast_i += 1

        ans = ""
        for i in range(len(s)):
            if s[i] != "*" and i not in deleted_i:
                ans += s[i]

        return ans


sol = Solution()
print(sol.clearStars(s="aaba*"))
print(sol.clearStars(s="abc"))
