class Solution:
    def clearDigits(self, s: str) -> str:
        st: list[str] = []

        for c in s:
            if c.isdigit():
                if st:
                    st.pop()
            else:
                st.append(c)

        return "".join(st)


sol = Solution()
print(sol.clearDigits(s="abc"))
print(sol.clearDigits(s="cb34"))
print(sol.clearDigits(s="cb3"))
print(sol.clearDigits(s="cb335c"))
