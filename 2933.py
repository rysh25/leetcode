from collections import defaultdict, deque


class Solution:
    def findHighAccessEmployees(self, access_times: list[list[str]]) -> list[str]:
        a: list[tuple[int, str]] = []
        # print(f"access_times={access_times}")
        n = len(access_times)
        for e, time in access_times:
            a.append((int(time), e))

        a.sort()
        # print(f"a: {a}")

        q: deque[tuple[int, str]] = deque()
        employee_access_freq: defaultdict[str, int] = defaultdict(int)

        ans: set[str] = set()
        i = 0
        while i < n:
            current_time, ce = a[i]
            # print(f"current_time={current_time}, ce={ce}")
            q.append((current_time, ce))

            # if q:
            #     print("top: {q[0][0]} ({q[0][1]})")

            while q and q[0][0] <= current_time - 100:
                _, pe = q.popleft()
                # print(f"pop: {pe}")
                employee_access_freq[pe] -= 1

            employee_access_freq[ce] += 1

            if employee_access_freq[ce] >= 3:
                # print(f"!add: {ce}, freq={employee_access_freq[ce]}")
                ans.add(ce)
            i += 1

        return list(ans)


sol = Solution()
print(
    sol.findHighAccessEmployees(
        access_times=[
            ["a", "0549"],
            ["b", "0457"],
            ["a", "0532"],
            ["a", "0621"],
            ["b", "0540"],
        ]
    )
)
print(
    sol.findHighAccessEmployees(
        access_times=[
            ["d", "0002"],
            ["c", "0808"],
            ["c", "0829"],
            ["e", "0215"],
            ["d", "1508"],
            ["d", "1444"],
            ["d", "1410"],
            ["c", "0809"],
        ]
    )
)
print(
    sol.findHighAccessEmployees(
        access_times=[
            ["cd", "1025"],
            ["ab", "1025"],
            ["cd", "1046"],
            ["cd", "1055"],
            ["ab", "1124"],
            ["ab", "1120"],
        ]
    )
)


print(
    sol.findHighAccessEmployees(
        access_times=[
            ["akuhmu", "0454"],
            ["aywtqh", "0523"],
            ["akuhmu", "0518"],
            ["ihhkc", "0439"],
            ["ihhkc", "0508"],
            ["akuhmu", "0529"],
            ["aywtqh", "0530"],
            ["aywtqh", "0419"],
        ]
    )
)  # ["akuhmu"]


print(
    sol.findHighAccessEmployees(
        access_times=[
            ["qzgyyji", "1945"],
            ["qzgyyji", "1855"],
            ["jsxkxtugi", "1859"],
            ["hhjuaxal", "1940"],
            ["hhjuaxal", "1831"],
            ["jsxkxtugi", "1841"],
            ["hhjuaxal", "1918"],
            ["jsxkxtugi", "1941"],
            ["hhjuaxal", "1852"],
        ]
    )
)  # ["hhjuaxal"]
