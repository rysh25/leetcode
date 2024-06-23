class Solution:
    def countCompleteDayPairs(self, hours: list[int]) -> int:
        counts = [0] * 25
        n = len(hours)
        for i in range(n):
            hours[i] %= 24
            hours[i] = 24 if hours[i] == 0 else hours[i]

            counts[hours[i]] += 1

        # print(f"counts={counts}")

        ans = 0
        for i in range(1, 12):
            if counts[i] > 0 and counts[24 - i] > 0:
                # print(f"i={i}")
                ans += counts[i] * counts[24 - i]

        if counts[12] > 1:
            ans += counts[12] * (counts[12] - 1) // 2

        if counts[24] > 1:
            ans += counts[24] * (counts[24] - 1) // 2

        return ans


sol = Solution()
print(sol.countCompleteDayPairs(hours=[12, 12, 30, 24, 24]))
print(sol.countCompleteDayPairs(hours=[72, 48, 24, 3]))
print(sol.countCompleteDayPairs(hours=[1, 6]))  # 0
print(sol.countCompleteDayPairs(hours=[21, 19, 3]))  # 1
