class Solution:
    def winningPlayerCount(self, n: int, pick: list[list[int]]) -> int:
        wins: list[list[int]] = [[0] * 11 for _ in range(n)]

        for p in pick:
            wins[p[0]][p[1]] += 1

        print(f"wins={wins}")

        ans = 0

        for i, w in enumerate(wins):
            for j in range(11):
                if w[j] > i:
                    ans += 1
                    break

        return ans


sol = Solution()
# print(
#     sol.winningPlayerCount(n=4, pick=[[0, 0], [1, 0], [1, 0], [2, 1], [2, 1], [2, 0]])
# )
# print(sol.winningPlayerCount(n=5, pick=[[1, 1], [1, 2], [1, 3], [1, 4]]))
# print(sol.winningPlayerCount(n=5, pick=[[1, 1], [2, 4], [2, 4], [2, 4]]))
# print(sol.winningPlayerCount(n=4, pick=[[3, 3]]))
# print(sol.winningPlayerCount(n=2, pick=[[0, 8], [0, 3]]))  # 1
# print(sol.winningPlayerCount(n=3, pick=[[1, 3], [2, 10]]))  # 0
print(sol.winningPlayerCount(n=2, pick=[[1, 5], [0, 10], [1, 4]]))  # 1
