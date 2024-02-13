class Solution:
    def minimumPushes(self, word: str) -> int:
        ans = 0
        freq: list[int] = [0] * 26

        for i in range(len(word)):
            freq[ord(word[i]) - ord("a")] += 1

        freq2: list[tuple[int, int]] = []

        for i in range(len(freq)):
            freq2.append((freq[i], i))

        freq2.sort(reverse=True)

        ans = 0
        length = 1
        for i, (count, c) in enumerate(freq2):
            # print(f"i={i}, count={count}, length={length}, c={chr(c+ord('a'))}")
            ans += count * length
            if (i + 1) % 8 == 0:
                length += 1
        return ans


sol = Solution()
print(sol.minimumPushes(word="abcde"))
print(sol.minimumPushes(word="xyzxyzxyzxyz"))
print(sol.minimumPushes(word="aabbccddeeffgghhiiiiii"))
