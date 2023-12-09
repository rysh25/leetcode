class Solution:
    def countCompleteSubstrings(self, word: str, k: int) -> int:
        ans = 1

        if len(word) == 1:
            if k == 1:
                return 1
            else:
                return 0

        s: set[str] = set()

        freq = {k: 0 for k in range(26)}
        if k == 1:
            ans += 1
            s.add(word[0])
            l = 1
        else:
            l = 0
            freq[ord(word[0]) - ord("a")] += 1

        for r in range(1, len(word)):
            # print(
            #     f"r={r}, {word[r]}, freq[ord(word[r]) - ord('a')]={freq[ord(word[r]) - ord('a')]}"
            # )
            if abs(ord(word[r]) - ord(word[r - 1])) > 2:
                freq = {k: 0 for k in range(26)}
                l = r + 1
                continue

            freq[ord(word[r]) - ord("a")] += 1

            if freq[ord(word[r]) - ord("a")] > k:
                freq = {k: 0 for k in range(26)}
                l = r + 1
                continue

            complete = True
            for fk in freq:
                if freq[fk] != 0 and freq[fk] != k:
                    complete = False
                    break

            # print(f"complete={complete}")

            if complete:
                ans += 1
                freq = {k: 0 for k in range(26)}
                s.add(word[l : r + 1])
                l = r + 1
                # print(f"ans={ans}")

        print(f"s={s}")

        return (len(s) + 1) * len(s) // 2 if len(s) > 0 else 0


sol = Solution()
print(sol.countCompleteSubstrings(word="igigee", k=2))
print(sol.countCompleteSubstrings(word="aaabbbccc", k=3))
print(sol.countCompleteSubstrings(word="a", k=1))  # 1
print(sol.countCompleteSubstrings(word="ba", k=1))  # 3
print(sol.countCompleteSubstrings(word="abb", k=1))  # 4
