class Solution:
    def beautifulIndices(self, s: str, a: str, b: str, k: int) -> list[int]:
        a_is: list[int] = []
        b_is: list[int] = []

        for i in range(len(s)):
            if i + len(a) <= len(s) and a == s[i : i + len(a)]:
                a_is.append(i)
            if i + len(b) <= len(s) and b == s[i : i + len(b)]:
                b_is.append(i)

        # print(f"a_is={a_is}")
        # print(f"b_is={b_is}")

        ans: list[int] = []
        b_i = 0
        for a_i in range(len(a_is)):
            while (
                b_i < len(b_is)
                and abs(b_is[b_i] - a_is[a_i]) > k
                and a_is[a_i] > b_is[b_i]
            ):
                b_i += 1

            # print(f"b_i={b_i}")

            if b_i >= len(b_is):
                break

            if abs(b_is[b_i] - a_is[a_i]) <= k:
                ans.append(a_is[a_i])

        return ans


sol = Solution()
print(
    sol.beautifulIndices(
        s="isawsquirrelnearmysquirrelhouseohmy", a="my", b="squirrel", k=15
    )
)
print(sol.beautifulIndices(s="abcd", a="a", b="a", k=4))
print(sol.beautifulIndices(s="bavgoc", a="ba", b="c", k=6))  # [0]
print(sol.beautifulIndices(s="lahhnlwx", a="hhnlw", b="ty", k=6))  # []
print(sol.beautifulIndices(s="klxtee", a="e", b="klx", k=2))  # []
print(sol.beautifulIndices(s="frtzggff", a="g", b="f", k=1))  # []
