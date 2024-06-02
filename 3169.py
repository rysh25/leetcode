class Solution:
    def countDays(self, days: int, meetings: list[list[int]]) -> int:
        from collections import defaultdict

        schedule: defaultdict[int, int] = defaultdict(int)

        for meeting in meetings:
            schedule[meeting[0] - 1] += 1
            schedule[meeting[1]] -= 1

            if schedule[meeting[1]] == 0:
                del schedule[meeting[1]]

        print(f"schedule={sorted(schedule.items())}")

        curr = 0
        ans = 0
        curr = 0
        prev = 0
        prev_d = 0
        for d, _ in sorted(schedule.items()):
            curr += schedule[d]
            # print(f"d={d}, schedule[d]={schedule[d]}, prev={prev}, curr={curr}")
            if curr == 0:
                if prev > 0:
                    prev_d = d
            elif curr > 0:
                if prev == 0:
                    ans += d - prev_d

            prev = curr
            # print(f"i={i}, schedule[i]={schedule[i]}, curr={curr}, ans={ans}")

        if curr == 0:
            ans += days - prev_d

        return ans


sol = Solution()
print(sol.countDays(days=10, meetings=[[5, 7], [1, 3], [9, 10]]))
print(sol.countDays(days=5, meetings=[[2, 4], [1, 3]]))
print(sol.countDays(days=6, meetings=[[1, 6]]))
