class Solution:
    def findMinimumOperations(self, s1: str, s2: str, s3: str) -> int:
        n = min(len(s1), len(s2), len(s3))
        l = 0
        for i in range(n):
            if s1[i] == s2[i] == s3[i]:
                l += 1
            else:
                break

        # print(f"l={l}")
        if l < 1:
            return -1

        ans = 0
        if len(s1) > l:
            ans += len(s1) - l
        if len(s2) > l:
            ans += len(s2) - l
        if len(s3) > l:
            ans += len(s3) - l

        return ans


sol = Solution()
print(sol.findMinimumOperations(s1="abc", s2="abb", s3="ab"))
print(sol.findMinimumOperations(s1="dac", s2="bac", s3="cac"))
print(sol.findMinimumOperations(s1="a", s2="a", s3="a"))
print(sol.findMinimumOperations(s1="a", s2="aabc", s3="a"))  # 3
