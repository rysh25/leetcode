class Solution:
    def combinationSum2(self, candidates: list[int], target: int) -> list[list[int]]:
        """
        候補の数値の配列と、ターゲットの数値が渡されます。
        足すとターゲットとなる候補の配列内のすべての一意の組み合わせを返します。

        はじめに候補配列をソートします。
        バックトラックで再帰的に組み合わせを作成します。
        組み合わせの合計がターゲットと同じなら、結果の配列にその組み合わせを追加します。

        結果の配列には、重複する組み合わせを許さない。
        追加するタイミングで重複の確認をしようとすとそこで、O(n) の計算量が必要になるため、
        事前に、ソートを行いあらかじめ重複する数値の候補を除外するようにしている。


        Time complexity: O(2^n)
        Space complexity: O(n)

        Args:
            candidates (list[int]): 候補の数値の配列を指定します。
            target (int): ターゲットの数値を指定します。

        Returns:
            list[list[int]]: すべての一意の組み合わせの配列を返します。
        """
        ans: list[list[int]] = []
        candidates.sort()

        print(f"candidates={candidates}")

        def backtrack(index: int, curr: list[int], total: int):
            print(f"index={index}, curr={curr}, total={total}, target={target}")
            if total == target:
                ans.append(curr[:])
                return
            elif index >= len(candidates) or total > target:
                return

            prev = -1
            for i in range(index, len(candidates)):
                if prev == candidates[i]:
                    continue
                curr.append(candidates[i])
                backtrack(i + 1, curr, total + candidates[i])
                curr.pop()
                prev = candidates[i]

        backtrack(0, [], 0)

        return ans


sol = Solution()
# print(sol.combinationSum2(candidates=[10, 1, 2, 7, 6, 1, 5], target=8))
# print(sol.combinationSum2(candidates=[2, 5, 2, 1, 2], target=5))
print(sol.combinationSum2(candidates=[1, 1, 7], target=8))
