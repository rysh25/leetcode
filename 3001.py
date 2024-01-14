class Solution:
    def minMovesToCaptureTheQueen(
        self, a: int, b: int, c: int, d: int, e: int, f: int
    ) -> int:
        ans = 2

        if a == e:
            if a == c:
                if b < d < f:
                    ans = min(ans, 2)
                elif b > d > f:
                    ans = min(ans, 2)
                else:
                    ans = min(ans, 1)
            else:
                ans = min(ans, 1)
        if b == f:
            if b == d:
                if a < c < e:
                    ans = min(ans, 2)
                elif a > c > e:
                    ans = min(ans, 2)
                else:
                    ans = min(ans, 1)
            else:
                ans = min(ans, 1)
        if c + d == e + f:
            # print(f"a+b={a+b}, c+d={c+d}, e+f={e+f}")
            if c + d == a + b:
                if c < a < e:
                    ans = min(ans, 2)
                elif c > a > e:
                    ans = min(ans, 2)
                else:
                    ans = min(ans, 1)
            else:
                ans = min(ans, 1)
        if c - d == e - f:
            # print(f"a-b={a-b}, c-d={c-d}, e-f={e-f}")
            if c - d == a - b:
                if c < a < e:
                    ans = min(ans, 2)
                elif c > a > e:
                    ans = min(ans, 2)
                else:
                    ans = min(ans, 1)
            else:
                ans = min(ans, 1)

        return ans


sol = Solution()
# print(sol.minMovesToCaptureTheQueen(a=1, b=1, c=8, d=8, e=2, f=3))
# print(sol.minMovesToCaptureTheQueen(a=5, b=3, c=3, d=4, e=5, f=2))
print(sol.minMovesToCaptureTheQueen(a=1, b=1, c=1, d=4, e=1, f=8))  # 2
