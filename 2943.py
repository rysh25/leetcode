class Solution:
    def maximizeSquareHoleArea(
        self, n: int, m: int, hBars: list[int], vBars: list[int]
    ) -> int:
        max_h = 1
        max_v = 1
        hBars.sort()
        vBars.sort()

        prev_wall = 1
        prev = 1
        for i in range(0, len(hBars)):
            # print(f"hBars[i]={hBars[i]}, prev={prev}, prev_wall={prev_wall}")
            if hBars[i] - prev > 1:
                prev_wall = hBars[i] - 1
            # print(f"hBars[i] - prev_wall + 1={hBars[i] - prev_wall + 1}")
            max_h = max(max_h, hBars[i] - prev_wall + 1)
            prev = hBars[i]
        # print(f"max_h={max_h}")

        prev_wall = 1
        prev = 1
        for i in range(0, len(vBars)):
            # print(f"vBars[i]={vBars[i]}, prev={prev}, prev_wall={prev_wall}")
            if vBars[i] - prev > 1:
                prev_wall = vBars[i] - 1

            # print(f"vBars[i] - prev_wall + 1={vBars[i] - prev_wall + 1}")
            max_v = max(max_v, vBars[i] - prev_wall + 1)
            prev = vBars[i]
        # print(f"max_v={max_v}")

        return min(max_h, max_v) * min(max_h, max_v)


sol = Solution()
print(sol.maximizeSquareHoleArea(n=2, m=1, hBars=[2, 3], vBars=[2]))
print(sol.maximizeSquareHoleArea(n=1, m=1, hBars=[2], vBars=[2]))
print(sol.maximizeSquareHoleArea(n=2, m=3, hBars=[2, 3], vBars=[2, 3, 4]))
print(sol.maximizeSquareHoleArea(n=3, m=2, hBars=[3, 2, 4], vBars=[3, 2]))  # 9
print(
    sol.maximizeSquareHoleArea(n=4, m=40, hBars=[5, 3, 2, 4], vBars=[36, 41, 6, 34, 33])
)  # 9
print(sol.maximizeSquareHoleArea(n=14, m=4, hBars=[13], vBars=[3, 4, 5, 2]))  # 4
