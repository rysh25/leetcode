from typing import List


class Solution:
    def isValid(self, s: str) -> bool:
        """
        スタックを利用する
        開き括弧ならスタックにプッシュする。
        閉じ括弧ならポップして、対応する括弧でなければ False を返す。
        最後にスタックが空でなければ False を返す。
        そうでなければ True を返す。

        #Stack
        """
        stack: List[str] = []
        for c in s:
            # print(f"c={c}")
            if c == "(" or c == "{" or c == "[":
                stack.append(c)
            elif c == ")":
                if len(stack) == 0 or stack.pop() != "(":
                    return False
            elif c == "}":
                if len(stack) == 0 or stack.pop() != "{":
                    return False
            elif c == "]":
                if len(stack) == 0 or stack.pop() != "[":
                    return False

        if len(stack) == 0:
            return True

        return False


sol = Solution()
print(sol.isValid(s="()"))
print(sol.isValid(s="()[]{}"))
print(sol.isValid(s="(]"))
print(sol.isValid(s="(()"))
print(sol.isValid(s=")"))
