class Solution:
    def minCost(self, colors: str, neededTime: list[int]) -> int:
        """
        アリスはロープの上にn個の風船を並べています。
        0 から始まるインデックスの文字列 colors が与えられます。
        colors[i] は i 番目のバルーンの色です。

        アリスはロープをカラフルにしたいと考えています。
        彼女は、連続する 2 つの風船が同じ色になることを望まないため、ボブに助けを求めます。
        ボブはロープから風船をいくつか取り外して、ロープをカラフルにすることができます。
        ここで、neededTime[i] は、ボブがロープから i 番目の風船を取り除くのに必要な時間 (秒単位) です。

        ボブがロープをカラフルにするのに必要な最小時間を返します。

        Args:
            colors (str): バルーンの色を表す配列
            neededTime (list[int]): 風船を取り除くのに必要な時間表す配列

        Returns:
            int: ボブがロープをカラフルにするのに必要な最小時間を返します。
        """
        prev_color = ""
        count = 0
        max_time = 0
        sum_time = 0
        ans = 0
        for i in range(len(colors)):
            if prev_color != colors[i]:
                if count > 1:
                    ans += sum_time - max_time
                print(f"color={colors[i]}, count={count}")
                count = 0
                max_time = 0
                sum_time = 0
            max_time = max(max_time, neededTime[i])
            sum_time += neededTime[i]
            count += 1
            prev_color = colors[i]

        if count > 1:
            ans += sum_time - max_time
        return ans


sol = Solution()
print(sol.minCost(colors="abaac", neededTime=[1, 2, 3, 4, 5]))
print(sol.minCost(colors="abc", neededTime=[1, 2, 3]))
print(sol.minCost(colors="aabaa", neededTime=[1, 2, 3, 4, 1]))
