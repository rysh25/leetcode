from typing import List, Tuple


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        """
        日毎の気温を記録した配列 temperatures を受け取る。
        各日から気温が高くなるまでを記録する ans 配列を0で初期化する
        気温の低下 (Monotonic Descendingx` Stack) を管理するスタックを用意する。

        temperatures 配列を初日から順にループする:
            スタックの最新の気温より高ければ、順番にポップしながらループする:
                ポップした日付の ans のインデックスに現在日付との差を記録する
                (気温が高くなるまでの日数を記録)
            スタックに現在の日付の気温をプッシュする
        ans 配列を返却する

        単調スタック (Monotonic Stack) とは、
        ある要素A[i]の値よりも前(j<i)にあるより小さい最初の値 (降順の場合大きい値)
        A[j] を効率的に見つけるために利用するスタックのこと

        Time complexity: O(N)
        Space complexity: O(N)
        """

        ans: List[int] = [0] * len(temperatures)
        stack: List[Tuple[int, int]] = []  # (temprature, index)

        for i, temp in enumerate(temperatures):
            while stack and temp > stack[-1][0]:
                _, pop_index = stack.pop()
                ans[pop_index] = i - pop_index
            stack.append((temp, i))

        return ans


sol = Solution()
print(sol.dailyTemperatures(temperatures=[73, 74, 75, 71, 69, 72, 76, 73]))
print(sol.dailyTemperatures(temperatures=[30, 40, 50, 60]))
print(sol.dailyTemperatures(temperatures=[30, 60, 90]))
