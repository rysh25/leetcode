class Solution:
    def findChampion(self, grid: list[list[int]]) -> int:
        n = len(grid)
        max_wins = 0
        win_team = -1
        for i in range(n):
            wins = sum(grid[i])
            if wins >= max_wins:
                max_wins = wins
                win_team = i

        return win_team


sol = Solution()
print(sol.findChampion(grid=[[0, 1], [0, 0]]))
print(sol.findChampion(grid=[[0, 0, 1], [1, 0, 1], [0, 0, 0]]))
