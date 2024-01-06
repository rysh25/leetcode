class Solution:
    def jobScheduling(
        self, startTime: list[int], endTime: list[int], profit: list[int]
    ) -> int:
        """
        n個の仕事があり、各仕事はstartTime[i]からendTime[i]まで行う予定で、profit[i]の利益を得ます。

        startTime、endTime、profitの配列が与えられると、重複する時間範囲を持つ2つの仕事がないように、取ることができる最大の利益を返します。

        時間Xで終了する仕事を選択すると、時間Xで始まる別の仕事を開始できます。


        DP を利用する。
        事前に仕事を endTime の昇順にソートする。
        dp を n+1 の配列で用意する。
        dp[i+1] に ソートしたi番目までの仕事の最大の収益を記録していく
        dp[i+1] に、i番目の仕事の開始時間までに始められる仕事の最大の収益+i番目の仕事の収益を保存する。
        dp[n] が答えとなる。

        - Time complexity: O(n)
        - Space complexity: O(n)

        #DP
        #BinarySearch

        Args:
            startTime (list[int]): 仕事の開始時間を表す配列
            endTime (list[int]): 仕事の終了時間を表す配列
            profit (list[int]): 仕事の収益を表す配列

        Returns:
            int: 重複する時間範囲を持つ2つの仕事がないように、取ることができる最大の利益を返します。
        """
        n = len(startTime)

        jobs = sorted(zip(endTime, startTime, profit))

        jobs.sort()

        dp: list[int] = [0] * (n + 1)
        for i in range(n):
            # print(f"jobs[{i}]={jobs[i]}")
            l, r = -1, i + 1
            while r - l > 1:
                m = l + ((r - l) // 2)
                if jobs[m][0] <= jobs[i][1]:
                    l = m
                else:
                    r = m

            # print(f"i={i}, l={l}")
            if l >= 0:
                dp[i + 1] = max(dp[i], dp[l + 1] + jobs[i][2])
            else:
                dp[i + 1] = max(dp[i], jobs[i][2])
            # print(f"dp={dp}")
        return dp[n]


sol = Solution()
print(
    sol.jobScheduling(
        startTime=[1, 2, 3, 3], endTime=[3, 4, 5, 6], profit=[50, 10, 40, 70]
    )
)
print(
    sol.jobScheduling(
        startTime=[1, 2, 3, 4, 6],
        endTime=[3, 5, 10, 6, 9],
        profit=[20, 20, 100, 70, 60],
    )
)

print(
    sol.jobScheduling(
        startTime=[6, 15, 7, 11, 1, 3, 16, 2],
        endTime=[19, 18, 19, 16, 10, 8, 19, 8],
        profit=[2, 9, 1, 19, 5, 7, 3, 19],
    )
)  # 41
