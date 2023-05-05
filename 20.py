from typing import List


class Solution:
    def isValid(self, s: str) -> bool:
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
