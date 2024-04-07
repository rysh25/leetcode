class Solution:
    def getSmallestString(self, s: str, k: int) -> str:

        def distance(c1: str, c2: str):
            if ord(c1) < ord(c2):
                c1, c2 = c2, c1

            d1 = ord(c1) - ord(c2)
            d2 = ord(c2) + 26 - ord(c1)

            return min(d1, d2)

        n = len(s)

        ans = 0
        t = ""
        for i in range(n):
            for a in range(26):
                c = chr(ord("a") + a)
                d = distance(s[i], c)

                if ans + d <= k:
                    t += c
                    ans += d
                    break
        return t


sol = Solution()
print(sol.getSmallestString(s="zbbz", k=3))
print(sol.getSmallestString(s="xaxcd", k=4))
print(sol.getSmallestString(s="lol", k=0))
