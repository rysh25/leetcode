def is_vowel(c: str):
    if c in "aeiou":
        return True
    else:
        return False


class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        # print(f"s={s},k={k}")
        left, right = 0, 0
        vowels = 0
        max_vowels = 0
        while right < k:
            if is_vowel(s[right]):
                vowels += 1
            right += 1
        max_vowels = vowels

        # print(f"{s[left:right]}")
        # print(f"left={left}, right={right}, vowels={vowels}")

        while right < len(s):
            if is_vowel(s[left]):
                vowels -= 1
            left += 1
            if is_vowel(s[right]):
                vowels += 1
            right += 1

            # print(f"{s[left:right]}")
            # print(f"left={left}, right={right}, vowels={vowels}")
            max_vowels = max(max_vowels, vowels)

        return max_vowels


sol = Solution()
print(sol.maxVowels(s="abciiidef", k=3))
print(sol.maxVowels(s="aeiou", k=2))
print(sol.maxVowels(s="leetcode", k=3))
