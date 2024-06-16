class Solution:
    def findWinningPlayer(self, skills: list[int], k: int) -> int:
        n = len(skills)

        streak = 0
        win = 0
        for i in range(n - 1):
            if skills[win] < skills[i + 1]:
                win = i + 1
                streak = 1
            else:
                streak += 1

            if streak == k:
                return win

        return win


sol = Solution()
print(sol.findWinningPlayer(skills=[4, 2, 6, 3, 9], k=2))
print(sol.findWinningPlayer(skills=[2, 5, 4], k=3))
