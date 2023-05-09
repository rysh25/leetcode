from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        """
        n に指定された数値の適正な括弧のペアの組み合わせを全て作成して返します。

        DFS 的に再帰で全てを辿っていきます。
        各深さごとに、「(」と「)」の2股に分かれますが、「(」は、開いた数が n に
        到達するまで、「)」は、開いた数が、閉じた数より大きときのみ辿る様にします。

        再帰を辿る際に、スタックにプッシュし、戻ってきたら、ポップします。

        開いた数と、閉じた数が n と一致したら、括弧の組み合わせをリストにプッシュします。

        再帰を辿り終えたら、組み合わせリストを返します。

        Time complexity: O(2^n)
        Space complexity: O(n)

        #Stack
        """

        stack: List[str] = []
        ans: List[str] = []

        def dfs(open_n: int, close_n: int, depth: int = 0):
            if open_n == close_n == n:
                ans.append("".join(stack))
                return

            if open_n < n:
                stack.append("(")
                print(f"(: open_n={open_n}, close_n={close_n}, depth={depth}")
                dfs(open_n + 1, close_n, depth + 1)
                stack.pop()

            if close_n < open_n:
                stack.append(")")
                print(f"): open_n={open_n}, close_n={close_n}, depth={depth}")
                dfs(open_n, close_n + 1, depth + 1)
                stack.pop()

        dfs(0, 0)

        return ans


sol = Solution()
print(sol.generateParenthesis(n=3))
