class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        """
        個別の整数からなるの候補配列 candidates と、整数 target が指定されます。
        選択した数値の合計が target となる candidates の一意の組み合わせのリストを返します。

        candidate 内の数値は無制限に何度でも使うことができます。
        選択した数値の頻度が少なくとも1つ異なれば一意となります。

        - Time complexity: O(n*n^2)
        - Space complexity: O(n*n^2)

        #BackTracking

        Args:
            candidates (list[int]): 個別の数値からなるの候補配列をしています。
            target (int): 合計を指定します。

        Returns:
            list[list[int]]: 合計が target となる一意の数値の組み合わせを返します。
        """

        ans: list[list[int]] = []

        print(f"candidates={candidates}, target={target}")

        def backtrack(i: int, cur: list[int], total: int):
            if i >= len(candidates) or total > target:
                return
            elif total == target:
                ans.append(cur.copy())
                # print(f"total == target: cur={cur}, totoal={total}")
                return

            cur.append(candidates[i])
            # print(
            #     f"Push: i={i}, candidates[i]={candidates[i]}, cur={cur}, total={total}"
            # )
            backtrack(i, cur, total + candidates[i])

            cur.pop()
            # print(f"Pop: i={i},  cur={cur}, total={total}")
            backtrack(i + 1, cur, total)

        backtrack(0, [], 0)

        return ans


sol = Solution()
print(sol.combinationSum(candidates=[2, 3, 6, 7], target=7))
print(sol.combinationSum(candidates=[2, 3, 5], target=8))
print(sol.combinationSum(candidates=[2], target=1))
