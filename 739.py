class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        """
        各日の気温からなるの整数配列を元に、各日を基準に次に気温が高くなる日までの日数の
        配列を生成して返します。

        各日から気温が高くなるまでを記録する ans 配列を0で初期化する
        単調減少スタック (Monotonic Decreasing Stack) を用意します。

        単調スタック (Monotonic Stack) とは、下から小さな値スタックで、
        これを使うと、後の最も近いの大きな要素 (Nearest Greater to Right) を
        高速に見つけることができます。

        見つけた NGR の日付の差分を ans 配列の対応する要素に設定します。

        ans を返します。

        Time complexity: O(N)
        Space complexity: O(N)

        #Stack
        #MonotonicStack
        #NGR

        Args:
            temperatures (list[int]): 各日の気温からなるの整数配列を渡します。

        Returns:
            list[int]: temperatures の各日を基準に次に気温が高くなる日までの日数の配列を返します。
        """

        ans: list[int] = [0] * len(temperatures)
        stack: list[tuple[int, int]] = []  # (temprature, index)

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
