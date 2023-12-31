class Solution:
    def maximizeSquareArea(
        self, m: int, n: int, hFences: list[int], vFences: list[int]
    ) -> int:
        # print(f"m={m}, n={n}, hFences={hFences}, vFences={vFences}")
        ans = -1
        hFences.sort()
        vFences.sort()

        for i, hFence in enumerate([1] + hFences):
            # print(f"hFence={hFence}")
            for j, vFence in enumerate([1] + vFences):
                # print(f"vFence={vFence}")
                ii, ij = i, j
                while ii <= len(hFences) and ij <= len(vFences):
                    # print(f"i={i}, j={j}, ii={ii}, ij={ij}")
                    h, v = 0, 0
                    if ii < len(hFences):
                        h = hFences[ii] - hFence
                    else:
                        h = m - hFence

                    if ij < len(vFences):
                        v = vFences[ij] - vFence
                    else:
                        v = n - vFence

                    if h == v:
                        # print(f"h={h}, v={v}")
                        ans = max(ans, h * v)

                    if h >= v:
                        ij += 1
                    else:
                        ii += 1
        return ans


sol = Solution()
print(sol.maximizeSquareArea(m=4, n=3, hFences=[2, 3], vFences=[2]))
print(sol.maximizeSquareArea(m=6, n=7, hFences=[2], vFences=[4]))
print(sol.maximizeSquareArea(m=3, n=9, hFences=[2], vFences=[8, 6, 5, 4]))  # 4
