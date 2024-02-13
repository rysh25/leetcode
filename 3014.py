class Solution:
    def minimumPushes(self, word: str) -> int:
        ans = 0
        n = len(word)
        i = 1
        while n > 0:
            # print(f"n={n}, (n % 9)={(n % 9)}, i={i}, ans={ans}")
            if n >= 8:
                ans += 8 * i
            else:
                ans += (n % 8) * i
            i += 1
            n -= 8
        return ans


sol = Solution()
print(sol.minimumPushes(word="abcde"))
print(sol.minimumPushes(word="abcdefghi"))
print(sol.minimumPushes(word="xycdefghij"))
print(sol.minimumPushes(word="abcdefghijklmnopqrstuvwxyz"))
