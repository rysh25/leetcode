from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        """
        スタックを使って逆ポーランド記法 (Reverse Polish Notation: RPN) を評価する。

        値をスタックに値を積み、演算子であれば取り出して評価する。
        評価結果をさらにスタックに積むという繰り返しを行う。

        Time complexity: O(n)
        Space complexity: O(n)

        #Stack
        """
        s: List[int] = []
        for t in tokens:
            if t == "+":
                b = s.pop()
                a = s.pop()
                s.append(a + b)
            elif t == "-":
                b = s.pop()
                a = s.pop()
                s.append(a - b)
            elif t == "*":
                b = s.pop()
                a = s.pop()
                s.append(a * b)
            elif t == "/":
                b = s.pop()
                a = s.pop()
                s.append(int(a / b))
            else:
                s.append(int(t))

            # print(f"t={t}, s={s}")
        if len(s) == 1:
            return s[0]
        else:
            return -1


sol = Solution()
print(sol.evalRPN(tokens=["2", "1", "+", "3", "*"]))
print(sol.evalRPN(tokens=["4", "13", "5", "/", "+"]))
print(
    sol.evalRPN(
        tokens=["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
    )
)
