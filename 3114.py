class Solution:
    def findLatestTime(self, s: str) -> str:

        for i in range(len(s)):
            if i == 2:
                continue

            if s[i] == "?":
                if i == 0:
                    if s[1] < "2" or s[1] == "?":
                        s = s[:0] + "1" + s[1:]
                    else:
                        s = s[:0] + "0" + s[1:]
                elif i == 1:
                    if s[0] == "1":
                        s = s[:1] + "1" + s[2:]
                    else:
                        s = s[:1] + "9" + s[2:]
                if i == 3:
                    s = s[:3] + "5" + s[4:]
                elif i == 4:
                    s = s[:4] + "9"

        return s


sol = Solution()
print(sol.findLatestTime(s="1?:?4"))
print(sol.findLatestTime(s="0?:5?"))
print(sol.findLatestTime(s="0?:??"))
print(sol.findLatestTime(s="0?:0?"))
print(sol.findLatestTime(s="?9:??"))
print(sol.findLatestTime(s="??:??"))
print(sol.findLatestTime(s="0?:??"))
print(sol.findLatestTime(s="?3:12"))  # "03:12"
