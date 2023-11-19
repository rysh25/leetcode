class Solution:
    def reductionOperations(self, nums: list[int]) -> int:
        """
        整数配列 nums が与えられた場合、目標は nums 内のすべての要素を等しくすることです。
        1 つの操作を完了するには、次の手順に従います。

        1. nums の最大値を見つけます。 そのインデックスを i (0 から始まるインデックス) とし、その値を largest とします。 最大値を持つ要素が複数ある場合は、最小の i を選択します。
        2. largest より厳密に小さい数値で次に大きい値を見つけます。 その値を nextLargest とします。
        3. nums[i] を nextLargest まで減らします。

        nums 内のすべての要素を等しくするための処理の数を返します。


        一番小さい値の次の大きな値の操作回数は1、その次に大きな値の操作回数は2と値が増えるごとに操作回数も増える。
        そのため、nums を昇順にソートし、小さいものから順に値が増えるごとに操作回数を増やしていき、全体の操作回数を合計する。


        - Time complexity: O(n)
        - Space complexity: O(n)

        Args:
            nums (list[int]): _description_

        Returns:
            int: nums 内のすべての要素を等しくするための処理の数を返します。
        """
        nums.sort()
        step = 0
        ans = 0
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                step += 1
            ans += step

        return ans


sol = Solution()
print(sol.reductionOperations(nums=[5, 1, 3]))
print(sol.reductionOperations(nums=[1, 1, 1]))
print(sol.reductionOperations(nums=[1, 1, 2, 2, 3]))
