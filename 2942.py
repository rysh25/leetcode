class Solution:
    def findWordsContaining(self, words: list[str], x: str) -> list[int]:
        ans: list[int] = []
        for i, word in enumerate(words):
            if x in word:
                ans.append(i)
        return ans


sol = Solution()
print(sol.findWordsContaining(words=["leet", "code"], x="e"))
print(sol.findWordsContaining(words=["abc", "bcd", "aaaa", "cbc"], x="a"))
print(sol.findWordsContaining(words=["abc", "bcd", "aaaa", "cbc"], x="z"))
