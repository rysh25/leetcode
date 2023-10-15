class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        n = len(s)
        ans = ""
        l, r = 0, 0
        length = 101
        count = 1 if s[r] == "1" else 0
        while l <= r and r < n:
            # print(f"l={l}, r={r}, s[l:r+1]={s[l:r+1]}, count={count}")

            if count == k:
                if r - l < length:
                    length = r - l
                    ans = s[l : r + 1]
                if r - l == length:
                    ans = min(ans, s[l : r + 1])

            if count >= k:
                if s[l] == "1":
                    count -= 1
                l += 1
            else:
                r += 1
                if r < n and s[r] == "1":
                    count += 1
        return ans


sol = Solution()
print(sol.shortestBeautifulSubstring(s="100011001", k=3))
print(sol.shortestBeautifulSubstring(s="1011", k=2))
print(sol.shortestBeautifulSubstring(s="000", k=1))
