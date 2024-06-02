class Solution:
    def compressedString(self, word: str) -> str:
        comp = ""

        last = ""
        streak = 0
        for i in range(len(word) + 1):
            c = ""
            if i == len(word):
                c = ""
            else:
                c = word[i]

            if streak == 9 or (last != "" and c != last):
                comp += str(streak) + last
                streak = 1
            else:
                streak += 1

            last = c

        return comp


sol = Solution()
print(sol.compressedString(word="abcde"))
print(sol.compressedString(word="aaaaaaaaaaaaaabb"))
