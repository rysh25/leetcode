class Solution:
    def minOperations(self, s: str) -> int:
        """
        文字「0」と「1」のみからなる文字列 s が与えられます。
        1 回の操作で、任意の「0」を「1」に、またはその逆に変更できます。

        隣接する 2 つの文字が等しくない場合、その文字列は交互と呼ばれます。

        s を交互にするために必要な演算の最小数を返します。

        - Time complexity: O(n)
        - Space complexity: O(1)

        Args:
            s (str): 文字「0」と「1」のみからなる文字列

        Returns:
            int: s を交互にするために必要な演算の最小数を返します。
        """
        op = 0
        curr = 0
        for i in range(len(s)):
            if str(curr) != s[i]:
                op += 1
            curr ^= 1
        ans = op

        op = 0
        curr = 1
        for i in range(len(s)):
            if str(curr) != s[i]:
                op += 1
            curr ^= 1
        ans = min(ans, op)

        return ans


sol = Solution()
print(sol.minOperations(s="0100"))
print(sol.minOperations(s="10"))
print(sol.minOperations(s="1111"))
