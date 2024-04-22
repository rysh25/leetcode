class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        from collections import defaultdict

        lo: defaultdict[str, int] = defaultdict(int)
        up: defaultdict[str, int] = defaultdict(int)

        for c in word:
            if c.islower():
                lo[c] += 1
            elif c.isupper():
                up[c] += 1

        ans = 0

        for l in lo:
            if lo[l] > 0 and up[l.upper()] > 0:
                ans += 1

        return ans


sol = Solution()
print(sol.numberOfSpecialChars(word="aaAbcBC"))
print(sol.numberOfSpecialChars(word="abc"))
print(sol.numberOfSpecialChars(word="abBCab"))
