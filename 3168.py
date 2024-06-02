class Solution:
    def minimumChairs(self, s: str) -> int:
        curr = 0
        mx = 0
        for c in s:
            if c == "E":
                curr += 1
            else:
                curr -= 1
            # print(f"curr={curr}")
            mx = max(mx, curr)

        return mx


sol = Solution()
print(sol.minimumChairs(s="EEEEEEE"))
print(sol.minimumChairs(s="ELELEEL"))
