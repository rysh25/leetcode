class Solution:
    def removeAlmostEqualCharacters(self, word: str) -> int:
        n = len(word)
        ans = 0
        i = 0
        while i < n - 1:
            # print(f"i={i}")
            if abs(ord(word[i]) - ord(word[i + 1])) < 2:
                ans += 1
                i += 1
            i += 1

        return ans


sol = Solution()
print(sol.removeAlmostEqualCharacters(word="aaaaa"))
print(sol.removeAlmostEqualCharacters(word="abddez"))
print(sol.removeAlmostEqualCharacters(word="zyxyxyz"))
