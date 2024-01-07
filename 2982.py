class Solution:
    def maximumLength(self, s: str) -> int:
        freq: list[list[int]] = [[0] * (5 * 10**5 + 1) for _ in range(26)]
        # freq: list[list[int]] = [[0] * (10) for _ in range(26)]
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
                # for j in range(1, streak):
                #     freq[c][j] += streak - j + 1
                max_streak[c] = max(max_streak[c], streak)
                streak = 1
            prev = s[i]

        c = ord(prev) - ord("a")
        freq[c][streak] += 1
        # for j in range(1, streak):
        #     freq[c][j] += streak - j + 1
        max_streak[c] = max(max_streak[c], streak)

        # print(f"freq={freq}")
        ans = -1
        for i in range(26):
            count = 0
            for j in range(max_streak[i], 0, -1):
                count += freq[i][j]
                # print(f"i={chr(i+ord('a'))}, j={j}, count={count}")
                if count >= 3:
                    # print(
                    #     f"!!!!i={chr(i+ord('a'))}, j={j}, freq[i][j] + count={freq[i][j] + count}"
                    # )
                    ans = max(ans, j)
                    break
                count *= 2

        # print(f"freq={freq}")
        return ans


sol = Solution()
print(sol.maximumLength(s="aaaa"))
print(sol.maximumLength(s="abcdef"))
print(sol.maximumLength(s="abcaba"))
print(sol.maximumLength(s="abcccccdddd"))  # 3
print(sol.maximumLength(s="bbc"))  # -1
print(sol.maximumLength(s="jicja"))  # -1
