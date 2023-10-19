class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        """
         2 つの文字列 s と t を指定すると、両方を空のテキスト エディタに入力したときにそれらが等しい場合に true を返す。
         「#」はバックスペース文字を意味します。

        空のテキストをバックスペースした後、
        テキストは空のままになることに注意する。

        #Stack

        - Time complexity: O(n)
        - Space complexity: O(n)

        Args:
            s (str): 文字列
            t (str): 文字列

        Returns:
            bool: エディタに入力したときにそれらが等しい場合に true を返す。
        """

        def input_str(s: str) -> str:
            st: list[str] = []
            for i in range(len(s)):
                if s[i] == "#":
                    if len(st) > 0:
                        st.pop()
                    continue

                st.append(s[i])
            return "".join(st)

        return input_str(s) == input_str(t)


sol = Solution()
print(sol.backspaceCompare(s="ab#c", t="ad#c"))
print(sol.backspaceCompare(s="ab##", t="c#d#"))
print(sol.backspaceCompare(s="a#c", t="b"))
print(sol.backspaceCompare(s="", t="b"))
print(sol.backspaceCompare(s="#", t="b"))
print(sol.backspaceCompare(s="##", t="b#"))
