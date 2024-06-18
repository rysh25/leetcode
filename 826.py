class Solution:
    def maxProfitAssignment(
        self, difficulty: list[int], profit: list[int], worker: list[int]
    ) -> int:
        """
        n個の仕事とm人の労働者がいます。 difficulty、profit、workerの3つの配列が与えられます：

        - difficulty[i]とprofit[i]は、i番目の仕事の難易度と利益であり、
        - worker[j]はj番目の労働者の能力です（つまり、j番目の労働者は難易度がworker[j]以下の仕事のみを完了できます）。

        すべての労働者には最大で1つの仕事が割り当てられることができますが、1つの仕事は複数回完了することができます。

        - たとえば、3人の労働者が1ドル支払われる同じ仕事に取り組んだ場合、合計利益は3ドルになります。労働者がどの仕事も完了できない場合、彼らの利益は0ドルです。

        労働者を仕事に割り当てた後に達成できる最大の利益を返します。


        - Time complexty: O(n)
        - Space complexity: O(1)

        #TwoPointers
        #Greedy

        Args:
            difficulty (list[int]): 仕事の難易度
            profit (list[int]): 利益
            worker (list[int]): 労働者の能力

        Returns:
            int: 労働者を仕事に割り当てた後に達成できる最大の利益を返します。
        """

        n = len(difficulty)
        m = len(worker)

        work = [[d, p] for d, p in zip(difficulty, profit)]
        work.sort(key=lambda x: x[0])

        worker.sort()

        # print(f"work={work}")

        ans = 0
        max_profit = 0
        i, j = 0, 0
        while i < m:
            # print(f"i={i}, worker[i]={worker[i]}")
            while j < n and work[j][0] <= worker[i]:
                max_profit = max(max_profit, work[j][1])
                j += 1

            # print(f"max_profit={max_profit}")
            ans += max_profit

            i += 1

        return ans


sol = Solution()
# print(
#     sol.maxProfitAssignment(
#         difficulty=[2, 4, 6, 8, 10], profit=[10, 20, 30, 40, 50], worker=[4, 5, 6, 7]
#     )
# )
# print(
#     sol.maxProfitAssignment(
#         difficulty=[85, 47, 57], profit=[24, 66, 99], worker=[40, 25, 25]
#     )
# )
print(
    sol.maxProfitAssignment(
        difficulty=[13, 37, 58], profit=[4, 90, 96], worker=[34, 73, 45]
    )
)
