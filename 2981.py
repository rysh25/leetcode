class Solution:
    def maximumLength(self, s: str) -> int:
        freq: list[list[int]] = [[0] * (52) for _ in range(26)]
        max_streak: list[int] = [0] * 26

        streak = 1
        prev = s[0]

        for i in range(1, len(s)):
            c = ord(prev) - ord("a")
            if prev == s[i]:
                streak += 1
            else:
                # print(f"s[{i}]={s[i]}, c={c}, streak={streak}")
                freq[c][streak] += 1
                for j in range(1, streak):
                    freq[c][j] += streak - j + 1
                max_streak[c] = max(max_streak[c], streak)
                streak = 1
            prev = s[i]

        c = ord(prev) - ord("a")
        freq[c][streak] += 1
        for j in range(1, streak):
            freq[c][j] += streak - j + 1
        max_streak[c] = max(max_streak[c], streak)

        # print(f"freq={freq}")
        ans = -1
        for i in range(26):
            for j in range(max_streak[i], -1, -1):
                if freq[i][j] >= 3:
                    ans = max(ans, j)
                    break

        # print(f"freq={freq}")
        return ans


sol = Solution()
print(sol.maximumLength(s="aaaa"))
print(sol.maximumLength(s="abcdef"))
print(sol.maximumLength(s="abcaba"))
