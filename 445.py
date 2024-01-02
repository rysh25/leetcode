class Solution:
    def findContentChildren(self, g: list[int], s: list[int]) -> int:
        g.sort()
        s.sort()

        ans = 0
        gi, si = 0, 0

        while gi < len(g) and si < len(s):
            while si < len(s) and g[gi] > s[si]:
                si += 1

            if si < len(s) and g[gi] <= s[si]:
                gi += 1
                si += 1
                ans += 1

        return ans


sol = Solution()
print(sol.findContentChildren(g=[1, 2, 3], s=[1, 1]))
print(sol.findContentChildren(g=[1, 2], s=[1, 2, 3]))
