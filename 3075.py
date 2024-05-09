class Solution:
    def maximumHappinessSum(self, happiness: list[int], k: int) -> int:
        """
        長さ n の配列 happiness と正の整数 k が与えられます。

        n 人の子供がキューに並んでおり、i 番目の子供の幸福値は happiness[i]です。
        これらの n 人の子供から k 回で k 人の子供を選択したいとします。

        各ターンで、子供を選択すると、それまで選択されていないすべての子供の幸福値が 1 ずつ減少します。
        幸福値はマイナスになることはなく、プラスの場合にのみ減少することに注意してください。

        k 人の子供を選択することで達成できる、選択した子供の幸福値の最大合計を返します。

        - Time complexity: O(n log n + min(k, n))
        - Space complexity: O(1)

        #Sorting
        #Greedy

        Args:
            happiness (list[int]): i 番目の子供の幸福値は happiness[i]です。
            k (int): k 回で k 人の子供を選択したい

        Returns:
            int: k 人の子供を選択することで達成できる、選択した子供の幸福値の最大合計を返します。
        """
        n = len(happiness)
        happiness.sort(reverse=True)

        ans = 0
        for i in range(min(n, k)):
            ans += max(happiness[i] - i, 0)

        return ans


sol = Solution()
print(sol.maximumHappinessSum([1, 2, 3], k=2))
print(sol.maximumHappinessSum([1, 1, 1, 1], k=2))
print(sol.maximumHappinessSum([2, 3, 4, 5], k=1))
